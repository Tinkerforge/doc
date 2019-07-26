# -*- coding: utf-8 -*-
"""
    sphinx.domains.go
    ~~~~~~~~~~~~~~~~~~

    The Go language domain.

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

_identifier_re = re.compile(r'\b(~?[a-zA-Z_][a-zA-Z0-9_]*[\[\]]*)')
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

    def _parse_type(self):
        self.skip_ws()
        ptr = self.skip_string("*")
        self.skip_ws()

        array = self.skip_string("[")
        if array:
            self.skip_ws()
            if self.match(re.compile("\d*")):
                element_count = self.matched_text
            else:
                self.fail('Expected element count of array type')
            if not self.skip_string("]"):
                self.fail("Expected ']' as end of array type")
            self.skip_ws()
            element_type = self._parse_type()
            return "{ptr}[{count}]{type}".format(ptr='*' if ptr else '', type=element_type, count=element_count)

        if self.match(_identifier_re):
            type_ = self.matched_text
        else:
            self.fail('Expected type (identifier)')

        while self.skip_string("."):
            if self.match(_identifier_re):
                type_ += "." + self.matched_text
            else:
                self.fail('Expected type (identifier)')

        return "{ptr}{t}".format(ptr='*' if ptr else '', t=type_)

    def _parse_param(self):
        self.skip_ws()

        if self.match(_identifier_re):
            param_name = self.matched_text
        else:
            self.fail('Expected parameter name (identifier)')

        if param_name == "func": #closure parameter
            if not self.skip_string("("):
                self.fail('Expected "(" as start of a callback function parameter definition')
            params = []
            while not self.skip_string(')'):
                params.append(self._parse_param())
                self.skip_ws()
                self.skip_string(',')
            param_text = "func(" + ", ".join(p.astext() for p in params) + ")"
            return addnodes.desc_parameter(param_text, param_text)

        self.skip_ws()
        param_type = self._parse_type()

        param_text = "{name} {t}".format(name=param_name, t=param_type)
        return addnodes.desc_parameter(param_text,param_text)

    def parse_function(self):
        if not self.skip_string('func'):
            self.fail('Expected "func" as start of signature')

        self.skip_ws()

        is_method = False
        if self.skip_string('(*'):
            is_method = True
            if self.match(_identifier_re):
                device_name = self.matched_text
            else:
                self.fail('Expected device name (identifier)')
            self.skip_string(')')

        self.skip_ws()

        if self.match(_identifier_re):
            fn_name = self.matched_text
        else:
            self.fail('Expected function name (identifier)')

        if not is_method:
            if "New" in fn_name:
                device_name = fn_name.replace("New", "")
            else:
                self.fail('Found function ' + self.definition + ' which was neither a method nor a constructor (thus the bricklet name is unknown).')

        if not self.skip_string('('):
            self.fail('Expected "(" as start of parameter list')

        params = []
        while not self.skip_string(')'):
            params.append(self._parse_param())
            self.skip_ws()
            self.skip_string(',')

        self.skip_ws()

        returns = []
        if self.skip_string('('):
            while not self.skip_string(')'):
                returns.append(self._parse_param())
                self.skip_ws()
                self.skip_string(',')

        result = addnodes.desc_signature(self.definition)
        result['struct'] = "(*" + device_name + ")"
        result['fn'] = fn_name
        result += addnodes.desc_annotation("func ", "func ")
        if is_method:
            result += addnodes.desc_addname("(*" + device_name + ")", "(*" + device_name + ")")
            result += addnodes.desc_annotation(" ", " ")
        result += addnodes.desc_name(fn_name, fn_name)

        paramList = addnodes.desc_parameterlist()
        for param in params:
            paramList += param
        result += paramList

        if len(returns) > 0:
            result += addnodes.desc_annotation(" ", " ")
            returnList = addnodes.desc_parameterlist()
            for ret in returns:
                returnList += ret
            result += returnList

        return result

    def parse_constant(self):
        if self.match(_identifier_re):
            device_name = self.matched_text + "."
        else:
            self.fail('Expected device name (identifier)')

        if not self.skip_string("."):
            self.fail('Expected "." between device name and constant name')

        if self.match(_identifier_re):
            constant_name = self.matched_text
        else:
            self.fail('Expected constant name (identifier)')

        result = addnodes.desc_signature("const " + self.definition)
        result += addnodes.desc_addname(device_name, device_name)
        result += addnodes.desc_name(constant_name, constant_name)
        result['struct'] = device_name + constant_name
        result['fn'] = ''

        return result

    def assert_end(self):
        self.skip_ws()
        if not self.eof:
            self.fail('expected end of definition, got %r' %
                      self.definition[self.pos:])


class GoObject(ObjectDescription):
    """Description of a Go language object."""

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
        objects = self.env.domaindata['go']['objects']
        if len(signode['fn']) > 0:
            fullname = signode['struct'] + " " + signode['fn']
        else:
            fullname = signode['struct']
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
            signode['struct'] = rv['struct']
            signode['fn'] = rv['fn']
            parser.assert_end()
        except DefinitionError, e:
            self.env.warn(self.env.docname,
                          e.description, self.lineno)
            raise ValueError
        self.describe_signature(signode, rv)

        return rv

class GoFunctionObject(GoObject):
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


class GoConstantObject(GoObject):
    def get_index_text(self, name):
        if self.objtype == 'constant':
            return _('%s (Go constant)') % name
        return ''

    def parse_definition(self, parser):
        return parser.parse_constant()

    def describe_signature(self, signode, obj):
        for node in obj:
            signode += node

class GoXRefRole(XRefRole):
    def _fix_parens(self, env, has_explicit_title, title, target):
        # remove parentheses
        if not has_explicit_title and title.endswith('()'):
            title = title[:-2]
        # remove parentheses from the target too
        if target.endswith('()'):
            target = target[:-2]
        return title, target

    def process_link(self, env, refnode, has_explicit_title, title, target):
        refnode['go:parent'] = env.temp_data.get('go:parent')
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


class GoDomain(Domain):
    """Go language domain."""
    name = 'go'
    label = 'Go'
    object_types = {
        'function': ObjType(l_('function'), 'func')
    }

    directives = {
        'function': GoFunctionObject,
        'constant': GoConstantObject,
    }
    roles = {
        'func': GoXRefRole(fix_parens=True),
        'const': GoXRefRole(fix_parens=True)
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

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        name, obj, node = self.data['objects'][target]

        return make_refnode(builder, fromdocname, name, target, contnode, target)

    def get_objects(self):
        for refname, (docname, type, sig_node) in self.data['objects'].iteritems():
            yield (refname, refname, type, docname, refname, 1)

def setup(app):
    app.add_domain(GoDomain)
