# -*- coding: utf-8 -*-

import sphinx.writers.html
from sphinx import __version__ as sphinx_version
from packaging.version import Version

from sphinx import addnodes
from docutils import nodes

# Handle different Sphinx versions
sphinx_ver = Version(sphinx_version)

if sphinx_ver >= Version('4.0'):
    # Sphinx 4.0+ removed SmartyPantsHTMLTranslator, use HTML5Translator instead
    from sphinx.writers.html5 import HTML5Translator as BaseTranslator
else:
    BaseTranslator = sphinx.writers.html.SmartyPantsHTMLTranslator

# Handle versionlabels import (removed in Sphinx 7.0)
try:
    from sphinx.locale import versionlabels
except ImportError:
    # Sphinx 7.0+ moved this to sphinx.domains.changeset
    try:
        from sphinx.domains.changeset import versionlabels
    except ImportError:
        # Fallback for newer versions
        versionlabels = {
            'versionadded': 'New in version %s',
            'versionchanged': 'Changed in version %s',
            'deprecated': 'Deprecated since version %s',
        }


class CustomHTMLTranslator(BaseTranslator):
    def __init__(self, builder, *args, **kwds):
        BaseTranslator.__init__(self, builder, *args, **kwds)

        self.settings.field_name_limit = 0 # stop docutils.writers.html4css1 from wrapping field names
        
        # Sphinx 7.x compatibility - initialize attributes used by visit_desc_parameter
        if not hasattr(self, 'multi_line_parameter_list'):
            self.multi_line_parameter_list = False
        if not hasattr(self, 'is_first_param'):
            self.is_first_param = True
        if not hasattr(self, 'list_is_required_param'):
            self.list_is_required_param = []
        if not hasattr(self, 'param_group_index'):
            self.param_group_index = 0
        if not hasattr(self, 'max_optional_param_level'):
            self.max_optional_param_level = 0

    def visit_desc_parameterlist(self, node):
        # Determine opening/closing based on domain
        if '.mathematicadomain.' in str(node.__class__):
            open_paren, close_paren = '[', ']'
        elif '.shelldomain.' in str(node.__class__) or '.tvpldomain.' in str(node.__class__):
            open_paren, close_paren = '', ''
        else:
            open_paren, close_paren = '<big>(</big>', '<big>)</big>'
        
        # For Sphinx 7.x, use the parent's _visit_sig_parameter_list method
        if hasattr(self, '_visit_sig_parameter_list'):
            self._visit_sig_parameter_list(node, addnodes.desc_parameter, open_paren, close_paren)
        else:
            # Fallback for older Sphinx
            if open_paren:
                self.body.append(open_paren)
            self.first_param = 1
            self.optional_param_level = 0
            self.required_params_left = sum([isinstance(c, addnodes.desc_parameter)
                                             for c in node.children])
            self.param_separator = node.child_text_separator

    def depart_desc_parameterlist(self, node):
        # For Sphinx 7.x, use the parent's _depart_sig_parameter_list method
        if hasattr(self, '_depart_sig_parameter_list'):
            self._depart_sig_parameter_list(node)
        else:
            # Fallback for older Sphinx
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


def setup(app):
    # Register the custom translator for modern Sphinx
    if sphinx_ver >= Version('4.0'):
        app.set_translator('html', CustomHTMLTranslator_v12)
    elif sphinx_version.startswith('1.1'):
        sphinx.writers.html.SmartyPantsHTMLTranslator = CustomHTMLTranslator_v11
    else:
        sphinx.writers.html.SmartyPantsHTMLTranslator = CustomHTMLTranslator_v12
    
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
