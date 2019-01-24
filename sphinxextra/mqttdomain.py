# -*- coding: utf-8 -*-
"""
    sphinx.domains.mqtt
    ~~~~~~~~~~~~~~~~~~

    The MQTT language domain.

    :copyright: Copyright 2007-2010 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re
from copy import deepcopy

from docutils import nodes
from docutils.parsers.rst import directives


from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
from sphinx.domains import Domain, ObjType
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util.compat import Directive
from sphinx.util.docfields import Field, TypedField

from sphinxextra.utils import fixup_index_entry

_identifier_re = re.compile(r'\b(~?[a-zA-Z_][a-zA-Z0-9_]*[\[\]]*)')
_whitespace_re = re.compile(r'\s+(?u)')
_topic_re = re.compile(r'\s*(.*)/(.*)/(.*)/(.*)')

class DefinitionParser(object):
    def __init__(self, definition):
        self.definition = definition.strip()

    def fail(self, msg):
        raise DefinitionError('Invalid definition: %s\n  %s' %
            (msg, self.definition))

    def parse_function(self):
        splt = self.definition.replace("[/SUFFIX]", "").split('/')
        if len(splt) < 3:
            self.fail("Expected topic with at least 3 path elements")
        if len(splt) > 4:
            self.fail("Expected topic with at most 4 path elements")
        if len(splt) == 4:
            req_type, bricklet_name, uid_placeholder, fn_name = splt
        else:
            req_type, bricklet_name, fn_name = splt
            uid_placeholder = None
        
        result = addnodes.desc_signature(self.definition)
        result['req_type'] = req_type
        result['struct'] = bricklet_name
        result['fn'] = fn_name
        if uid_placeholder is not None:
            result['uid_placeholder'] = uid_placeholder

        result += addnodes.desc_addname(req_type + "/", req_type + "/")
        result += addnodes.desc_addname(bricklet_name + "/", bricklet_name + "/")
        if uid_placeholder is not None:
            result += addnodes.desc_addname(uid_placeholder + "/", uid_placeholder + "/")
        result += addnodes.desc_name(fn_name, fn_name)
        return result

trans = {
'en_US': {
    'Parameters': 'Request payload',
    'Output': 'Response payload',
    },
'de_DE': {
    'Parameters': 'Request-Payload',
    'Output': 'Response-Payload',
    }
}

class Translatable:
    app_config = None

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return trans[self.app_config.language][self.key]

class MQTTObject(ObjectDescription):
    """Description of a MQTT language object."""

    option_spec = {
        'noindex': directives.flag,
        'module': directives.unchanged,
    }

    doc_field_types = [
        TypedField('parameter', label=Translatable('Parameters'),
                   names=('param', 'parameter', 'arg', 'argument',
                          'keyword', 'kwarg', 'kwparam', 'request', 'register'),
                   typerolename='obj', typenames=('paramtype', 'type')),
        TypedField('returnvalue', label=Translatable('Output'),
                   names=('returns', 'return', 'response', 'callback'),
                   typerolename='obj', typenames=('paramtype', 'type')),
        Field('noreturnvalue', label=Translatable('Output'), has_arg=False,
              names=('noreturn',)),
    ]
    def needs_arglist(self):
        return False

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
        objects = self.env.domaindata['mqtt']['objects']
        if 'uid_placeholder' in signode:
            fullname = signode['req_type'] + "/" + signode['struct'] + "/" + signode['uid_placeholder'] + "/" + signode['fn']        
        else:
            fullname = signode['req_type'] + "/" + signode['struct'] + "/" + signode['fn']        
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
            signode['req_type'] = rv['req_type']
            signode['fn'] = rv['fn']
            if 'uid_placeholder' in rv:
                signode['uid_placeholder'] = rv['uid_placeholder']
        except DefinitionError, e:
            self.env.warn(self.env.docname,
                          e.description, self.lineno)
            raise ValueError
        self.describe_signature(signode, rv)

        return rv

class MQTTFunctionObject(MQTTObject):
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

class MQTTXRefRole(XRefRole):
    def _fix_parens(self, env, has_explicit_title, title, target):
        # remove parentheses
        if not has_explicit_title and title.endswith('()'):                
            title = title[:-2]
        # remove parentheses from the target too
        if target.endswith('()'):
            target = target[:-2]
        return title, target

    def process_link(self, env, refnode, has_explicit_title, title, target):
        refnode['mqtt:parent'] = env.temp_data.get('mqtt:parent')
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


class MQTTDomain(Domain):
    """MQTT language domain."""
    name = 'mqtt'
    label = 'MQTT'
    object_types = {
        'function': ObjType(l_('function'), 'func')
    }

    directives = {
        'function':     MQTTFunctionObject,    
    }
    roles = {
        'func' :  MQTTXRefRole(fix_parens=True),
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
        name, obj, node = self.data['objects'][target]

        return make_refnode(builder, fromdocname, name, target,
                                contnode, target)
    def get_objects(self):
        for refname, (docname, type, sig_node) in self.data['objects'].iteritems():
            yield (refname, refname, type, docname, refname, 1)

def setup(app):
    Translatable.app_config = app.config
    app.add_domain(MQTTDomain)