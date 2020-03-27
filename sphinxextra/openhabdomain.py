# -*- coding: utf-8 -*-
"""
    sphinx.domains.openhab
    ~~~~~~~~~~~~~~~~~~

    The openHAB language domain.

    :copyright: Copyright 2007-2010 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re
from copy import deepcopy

from docutils import nodes

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
from sphinx.domains import Domain, ObjType
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util.compat import Directive
from sphinx.util.docfields import TypedField

from sphinxextra.utils import fixup_index_entry

_identifier_re = re.compile(r'\b(~?[a-zA-Z_][a-zA-Z0-9_\.]*)')
_whitespace_re = re.compile(r'\s+(?u)')

class DefinitionParser(object):
    def __init__(self, definition):
        self.definition = definition.strip()
        self.pos = 0
        self.end = len(self.definition)
        self.last_match = None
        self._previous_state = (0, None)

    def fail(self, msg):
        raise DefinitionError('Invalid definition: %s [error at %d]\n  %s' %
            (msg, self.pos, self.definition))

    def match(self, regex):
        match = regex.match(self.definition, self.pos)
        if match is not None:
            self._previous_state = (self.pos, self.last_match)
            self.pos = match.end()
            self.last_match = match
            return True
        return False

    def skip_string(self, string):
        strlen = len(string)
        if self.definition[self.pos:self.pos + strlen] == string:
            self.pos += strlen
            return True
        return False

    def skip_ws(self):
        return self.match(_whitespace_re)

    @property
    def eof(self):
        return self.pos >= self.end

    @property
    def current_char(self):
        try:
            return self.definition[self.pos]
        except IndexError:
            return 'EOF'

    @property
    def matched_text(self):
        if self.last_match is not None:
            return self.last_match.group()

    def parse_type(self):
        return self._parse_type()

    def parse_channel(self):
        if self.match(_identifier_re):
            device = self.matched_text
        else:
            self.fail('Expected device (identifier)')
        if not self.skip_string('::'):
            self.fail('Expected :: between device and function')

        if self.match( re.compile('[^\n]*')):
            channel_name = self.matched_text
        #channel_name = self.definition
        self.skip_string(channel_name)

        result = addnodes.desc_signature(channel_name)
        result['name'] = channel_name
        result['device'] = device

        result += addnodes.desc_name(channel_name, channel_name)
        return result

    def parse_function(self):
        if self.match(_identifier_re):
            device = self.matched_text
        else:
            self.fail('Expected device (identifier)')
        if not self.skip_string('::'):
            self.fail('Expected :: between device and function')

        if self.match(_identifier_re):
            function_name = self.matched_text
        else:
            self.fail('Expected function name (identifier)')

        if not self.skip_string('('):
            self.fail('Expected "(" as start of parameter list')

        params = []

        while not self.skip_string(')'):
            if self.match(_identifier_re):
                type_ = self.matched_text
            else:
                self.fail('Expected parameter type (identifier)')
            if self.skip_string('[]'):
                type_ += '[]'

            self.skip_ws()
            if self.match(_identifier_re):
                name = self.matched_text
            else:
                self.fail('Expected parameter name (identifier)')

            param_text = "{t} {name}".format(t=type_, name=name)
            params.append(addnodes.desc_parameter(param_text,param_text))
            self.skip_string(',')
            self.skip_ws()

        result = addnodes.desc_signature(self.definition)
        result['name'] = function_name
        result['device'] = device

        result += addnodes.desc_name(function_name, function_name)
        paramList = addnodes.desc_parameterlist()
        for param in params:
            paramList += param

        result += paramList
        return result

    def parse_constant(self):
        if self.match(_identifier_re):
            device_name = self.matched_text
        else:
            self.fail('Expected device name (identifier)')

        if not self.skip_string('::'):
            self.fail('Expected "::"')

        if self.match(_identifier_re):
            constant_name = self.matched_text
        else:
            self.fail('Expected constant name (identifier)')

        if not self.skip_string(':'):
            self.fail('Expected ":"')
        t = self._parse_type()

        result = addnodes.desc_signature("pub const " + self.definition)
        # result['struct'] = device_name + "::"
        # result['fn'] = constant_name
        # result += addnodes.desc_annotation("pub const ", "pub const ")
        # result += addnodes.desc_addname(device_name + "::", device_name + "::")
        # result += addnodes.desc_name(constant_name, constant_name)
        # result += addnodes.desc_type(t)
        return result

    def assert_end(self):
        self.skip_ws()
        if not self.eof:
            self.fail('expected end of definition, got %r' %
                      self.definition[self.pos:])


class OpenHABObject(ObjectDescription):
    """Description of a openHAB language object."""

    def get_index_text(self, name_cls):
        if self.objtype == 'function':
            return _('%s() (built-in function)') % name_cls
        elif self.objtype == 'callback':
            return _('%s() (built-in callback)') % name_cls
        elif self.objtype == 'data':
            return _('%s (built-in variable)') % name_cls
        else:
            return ''

    def add_target_and_index(self, sigobj, sig, signode):
        objects = self.env.domaindata['openhab']['objects']
        fullname = signode['device'] + '::' + signode['name']
        #print("Fullname", fullname)
        #fullname = signode['name']
        signode['ids'].append(fullname)

        # has to happen _after_ the fullname is added to the signodes' ids, as note_explicit_target generates the html id-attributes (i.e. link anchors)
        self.state.document.note_explicit_target(signode)

        if fullname in objects:
            self.env.warn(
                    self.env.docname,
                    'duplicate object description of %s, ' % fullname +
                    'other instance in ' +
                    self.env.doc2path(objects[fullname][0]) +
                    ', use :noindex: for one of them',
                    self.lineno)
        objects[fullname] = (self.env.docname, self.objtype, signode)

        indextext = self.get_index_text(fullname)
        if indextext:
            self.indexnode['entries'].append(fixup_index_entry(('single', indextext, fullname, fullname, 'foobar')))

    def parse_definition(self, parser):
        raise NotImplementedError()

    def describe_signature(self, signode, arg):
        raise NotImplementedError()

    def handle_signature(self, sig, signode):
        parser = DefinitionParser(sig)
        try:
            rv = self.parse_definition(parser)
            signode['name'] = rv['name']
            signode['device'] = rv['device']
            parser.assert_end()
        except DefinitionError, e:
            self.env.warn(self.env.docname,
                          e.description, self.lineno)
            raise ValueError
        self.describe_signature(signode, rv)

        return rv

class OpenHABChannelObject(OpenHABObject):
    def parse_definition(self, parser):
        return parser.parse_channel()

    def describe_signature(self, signode, func):
        for node in func:
            signode += node

class OpenHABFunctionObject(OpenHABObject):
    def parse_definition(self, parser):
        return parser.parse_function()

    def describe_signature(self, signode, func):
        for node in func:
            signode += node

class DefinitionError(Exception):
    def __init__(self, description):
        self.description = description

    def __unicode__(self):
        return self.description

    def __str__(self):
        return unicode(self.encode('utf-8'))


class OpenHABConstantObject(OpenHABObject):
    def get_index_text(self, name):
        if self.objtype == 'constant':
            return _('%s (openHAB constant)') % name
        return ''

    def parse_definition(self, parser):
        return parser.parse_constant()

    def describe_signature(self, signode, obj):
        for node in obj:
            signode += node

class OpenHABXRefRole(XRefRole):
    def _fix_parens(self, env, has_explicit_title, title, target):
        # remove parentheses
        if not has_explicit_title and title.endswith('()'):
            title = title[:-2]
        # remove parentheses from the target too
        if target.endswith('()'):
            target = target[:-2]
        return title, target

    def process_link(self, env, refnode, has_explicit_title, title, target):
        refnode['openhab:parent'] = env.temp_data.get('openhab:parent')
        if not has_explicit_title:
            target = target.lstrip('~') # only has a meaning for the title
            # if the first character is a tilde, don't display the module/class
            # parts of the contents
            if title[:1] == '~':
                title = title[1:]
                dcolon = title.rfind('::')
                if dcolon != -1:
                    title = title[dcolon + 2:]
        return title, target


class OpenHABDomain(Domain):
    """openHAB language domain."""
    name = 'openhab'
    label = 'openHAB'
    object_types = {
        'function': ObjType(l_('function'), 'func'),
        'channel': ObjType(l_('channel'), 'chan')
    }

    directives = {
        'channel':     OpenHABChannelObject,
        'function':     OpenHABFunctionObject,
        'constant':     OpenHABConstantObject,
    }
    roles = {
        'func' :  OpenHABXRefRole(fix_parens=True),
        'chan' :  OpenHABXRefRole(fix_parens=True)
     }
    initial_data = {
        'objects': {},  # fullname -> docname, objtype
    }

    def clear_doc(self, docname):
        for fullname, (fn, _, _) in self.data['objects'].items():
            if fn == docname:
                del self.data['objects'][fullname]

    def _under_to_camel(self, string):
        splt = string.split("_")
        return "".join(x.title() for x in splt)

    def resolve_xref(self, env, fromdocname, builder,
                     typ, target, node, contnode):
        try:
            name, obj, node = self.data['objects'][target]
        except:
            print('\n'+ target)
            #return addnodes.compact_paragraph(text='Ich bin ein Test', children=[contnode])
            #raise Exception("Blah")
            return nodes.Text(data='Blah')
            #return make_refnode(builder, fromdocname, fromdocname, target,
            #                    contnode, 'Titeltest')
            #pass

        return make_refnode(builder, fromdocname, name, target,
                                contnode, target)
    def get_objects(self):
        for refname, (docname, type, sig_node) in self.data['objects'].iteritems():
            yield (refname, refname, type, docname, refname, 1)

def setup(app):
    app.add_domain(OpenHABDomain)
