# -*- coding: utf-8 -*-

import sphinx.writers.html
from sphinx.locale import versionlabels
from sphinx import __version__ as sphinx_version

from sphinx import addnodes
from docutils import nodes

BaseTranslator = sphinx.writers.html.SmartyPantsHTMLTranslator

class CustomHTMLTranslator(BaseTranslator):
    def __init__(self, builder, *args, **kwds):
        BaseTranslator.__init__(self, builder, *args, **kwds)

    def visit_desc_parameterlist(self, node):
        if '.mathematicadomain.' in str(node.__class__):
            self.body.append('[')
        elif '.shelldomain.' not in str(node.__class__) and '.tvpldomain.' not in str(node.__class__):
            self.body.append('<big>(</big>')

        self.first_param = 1
        self.optional_param_level = 0
        # How many required parameters are left.
        self.required_params_left = sum([isinstance(c, addnodes.desc_parameter)
                                         for c in node.children])
        self.param_separator = node.child_text_separator

    def depart_desc_parameterlist(self, node):
        if '.mathematicadomain.' in str(node.__class__):
            self.body.append(']')
        elif '.shelldomain.' not in str(node.__class__) and '.tvpldomain.' not in str(node.__class__):
            self.body.append('<big>)</big>')

    def visit_emphasis(self, node):
        # don't add an <em> tag around external references
        if not isinstance(node.parent, nodes.reference):
            BaseTranslator.visit_emphasis(self, node)

    def depart_emphasis(self, node):
        # don't add an <em> tag around external references
        if not isinstance(node.parent, nodes.reference):
            BaseTranslator.depart_emphasis(self, node)

class CustomHTMLTranslator_v11(CustomHTMLTranslator):
    def __init__(self, builder, *args, **kwds):
        CustomHTMLTranslator.__init__(self, builder, *args, **kwds)

    def visit_versionmodified(self, node):
        self.body.append(self.starttag(node, 'p', CLASS=node['type']))
        text = versionlabels[node['type']] % node['version'].replace('$nbsp;', '&nbsp;')
        if len(node):
            text += ': '
        else:
            text += '.'
        self.body.append('<span class="versionmodified">%s</span>' % text)

    def depart_versionmodified(self, node):
        self.body.append('</p>\n')

class CustomHTMLTranslator_v12(CustomHTMLTranslator):
    def __init__(self, builder, *args, **kwds):
        CustomHTMLTranslator.__init__(self, builder, *args, **kwds)

    def bulk_text_processor(self, text):
        if '$nbsp;' in text:
            text = text.replace('$nbsp;', '&nbsp;')
        return text

if sphinx_version.startswith('1.2'):
    sphinx.writers.html.SmartyPantsHTMLTranslator = CustomHTMLTranslator_v12
else:
    sphinx.writers.html.SmartyPantsHTMLTranslator = CustomHTMLTranslator_v11

def setup(app):
    pass
