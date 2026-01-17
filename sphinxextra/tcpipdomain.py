# -*- coding: utf-8 -*-
"""
    sphinx.domains.tcpip
    ~~~~~~~~~~~~~~~~~~~~~

    The TCP/IP domain.

    :copyright: Copyright 2007-2010 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import _
from sphinx.domains import Domain, ObjType, Index
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from docutils.parsers.rst import Directive
from sphinx.util.docfields import Field, GroupedField, TypedField

from sphinxextra.utils import fixup_index_entry

trans = {
'en_US': {
    'Value': 'Value',
    'Function ID': 'Function ID',
    'Request': 'Request',
    'Response': 'Response'
    },
'de_DE': {
    'Value': 'Wert',
    'Function ID': 'Funktions ID',
    'Request': 'Anfrage',
    'Response': 'Antwort'
    }
}

class Translatable:
    app_config = None

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return trans[self.app_config.language][self.key]

# REs for TCP/IP signatures
tcpip_sig_re = re.compile(
    r'''^ ([\w.]*\.)?            # class name(s)
          (\w+)  \s*             # thing name
          (?: \((.*)\)           # optional: arguments
           (?:\s* -> \s* (.*))?  #           return annotation
          )? $                   # and nothing more
          ''', re.VERBOSE)

tcpip_paramlist_re = re.compile(r'([\[\],])')  # split at '[', ']' and ','


class TCPIPObject(ObjectDescription):
    """
    Description of a general TCP/IP object.
    """
    option_spec = {
        'noindex': directives.flag,
        'module': directives.unchanged,
    }

    doc_field_types = [
        Field('value', label=Translatable('Value'), has_arg=False,
              names=('value',)),
        Field('functionid', label=Translatable('Function ID'), has_arg=False,
              names=('functionid',)),
        Field('emptyrequest', label=Translatable('Request'), has_arg=False,
              names=('emptyrequest',)),
        Field('emptyresponse', label=Translatable('Response'), has_arg=False,
              names=('emptyresponse',)),
        Field('noresponse', label=Translatable('Response'), has_arg=False,
              names=('noresponse',)),
        TypedField('parameter', label=Translatable('Request'),
                   names=('param', 'parameter', 'arg', 'argument',
                          'keyword', 'kwarg', 'kwparam', 'request'),
                   typerolename='obj', typenames=('paramtype', 'type')),
        TypedField('returnvalue', label=Translatable('Response'),
              names=('returns', 'return', 'response'),
                   typerolename='obj', typenames=('paramtype', 'type')),
    ]

    def get_signature_prefix(self, sig):
        """
        May return a prefix to put before the object name in the signature.
        """
        return ''

    def needs_arglist(self):
        """
        May return true if an empty argument list is to be generated even if
        the document contains none.
        """
        return False

    def handle_signature(self, sig, signode):
        """
        Transform a TCP/IP signature into RST nodes.
        Returns (fully qualified name of the thing, classname if any).

        If inside a class, the current class name is handled intelligently:
        * it is stripped from the displayed name if present
        * it is added to the full name (return value) if not present
        """
        m = tcpip_sig_re.match(sig)
        if m is None:
            print('FAILED', sig)
            raise ValueError
        name_prefix, name, arglist, retann = m.groups()

        # determine module and class name (if applicable), as well as full name
        modname = self.options.get(
            'module', self.env.temp_data.get('tcpip:module'))
        classname = self.env.temp_data.get('tcpip:class')
        if classname:
            add_module = False
            if name_prefix and name_prefix.startswith(classname):
                fullname = name_prefix + name
                # class name is given again in the signature
                name_prefix = name_prefix[len(classname):].lstrip('.')
            elif name_prefix:
                # class name is given in the signature, but different
                # (shouldn't happen)
                fullname = classname + '.' + name_prefix + name
            else:
                # class name is not given in the signature
                fullname = classname + '.' + name
        else:
            add_module = True
            if name_prefix:
                classname = name_prefix.rstrip('.')
                fullname = name_prefix + name
            else:
                classname = ''
                fullname = name

        signode['module'] = modname
        signode['class'] = classname
        signode['fullname'] = fullname

        sig_prefix = self.get_signature_prefix(sig)
        if sig_prefix:
            signode += addnodes.desc_annotation(sig_prefix, sig_prefix)

        if name_prefix:
            signode += addnodes.desc_addname(name_prefix, name_prefix)
        # exceptions are a special case, since they are documented in the
        # 'exceptions' module.
        elif add_module and self.env.config.add_module_names:
            modname = self.options.get(
                'module', self.env.temp_data.get('tcpip:module'))
            if modname and modname != 'exceptions':
                nodetext = modname + '.'
                signode += addnodes.desc_addname(nodetext, nodetext)

        signode += addnodes.desc_name(name, name)
        if not arglist:
            if self.needs_arglist():
                # for callables, add an empty parameter list
                signode += addnodes.desc_parameterlist()
            if retann:
                signode += addnodes.desc_returns(retann, retann)
            return fullname, name_prefix
        signode += addnodes.desc_parameterlist()

        stack = [signode[-1]]
        for token in tcpip_paramlist_re.split(arglist):
            if token == '[':
                opt = addnodes.desc_optional()
                stack[-1] += opt
                stack.append(opt)
            elif token == ']':
                try:
                    stack.pop()
                except IndexError:
                    raise ValueError
            elif not token or token == ',' or token.isspace():
                pass
            else:
                token = token.strip()
                stack[-1] += addnodes.desc_parameter(token, token)
        if len(stack) != 1:
            raise ValueError
        if retann:
            signode += addnodes.desc_returns(retann, retann)
        return fullname, name_prefix

    def get_index_text(self, modname, name):
        """
        Return the text for the index entry of the object.
        """
        raise NotImplementedError('must be implemented in subclasses')

    def add_target_and_index(self, name_cls, sig, signode):
        modname = self.options.get(
            'module', self.env.temp_data.get('tcpip:module'))
        fullname = (modname and modname + '.' or '') + name_cls[0]
        # note target
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['tcpip']['objects']
            if fullname in objects:
                self.env.warn(
                    self.env.docname,
                    'duplicate object description of %s, ' % fullname +
                    'other instance in ' +
                    self.env.doc2path(objects[fullname][0]) +
                    ', use :noindex: for one of them',
                    self.lineno)
            objects[fullname] = (self.env.docname, self.objtype)

        indextext = self.get_index_text(modname, name_cls)
        if indextext:
            self.indexnode['entries'].append(fixup_index_entry(('single', indextext, fullname, fullname, 'foobar')))

    def before_content(self):
        # needed for automatic qualification of members (reset in subclasses)
        self.clsname_set = False

    def after_content(self):
        if self.clsname_set:
            self.env.temp_data['tcpip:class'] = None


class TCPIPModulelevel(TCPIPObject):
    """
    Description of an object on module level (functions, data).
    """

    def needs_arglist(self):
        return False #self.objtype == 'function' # Matthias: No argument list

    def get_index_text(self, modname, name_cls):
        if self.objtype == 'function':
            if not modname:
                return _('%s (built-in function)') % name_cls[0]
            return _('%s (in module %s)') % (name_cls[0], modname)
        elif self.objtype == 'data':
            if not modname:
                return _('%s (built-in variable)') % name_cls[0]
            return _('%s (in module %s)') % (name_cls[0], modname)
        else:
            return ''


class TCPIPClasslike(TCPIPObject):
    """
    Description of a class-like object (classes, interfaces, exceptions).
    """

    def get_signature_prefix(self, sig):
        return self.objtype + ' '

    def get_index_text(self, modname, name_cls):
        if self.objtype == 'class':
            if not modname:
                return _('%s (built-in class)') % name_cls[0]
            return _('%s (class in %s)') % (name_cls[0], modname)
        elif self.objtype == 'exception':
            return name_cls[0]
        else:
            return ''

    def before_content(self):
        TCPIPObject.before_content(self)
        if self.names:
            self.env.temp_data['tcpip:class'] = self.names[0][0]
            self.clsname_set = True


class TCPIPClassmember(TCPIPObject):
    """
    Description of a class member (methods, attributes).
    """

    def needs_arglist(self):
        return False #self.objtype.endswith('method') # Matthias: No argument list

    def get_signature_prefix(self, sig):
        if self.objtype == 'staticmethod':
            return 'static '
        elif self.objtype == 'classmethod':
            return 'classmethod '
        return ''

    def get_index_text(self, modname, name_cls):
        name, cls = name_cls
        add_modules = self.env.config.add_module_names
        if self.objtype == 'method':
            try:
                clsname, methname = name.rsplit('.', 1)
            except ValueError:
                if modname:
                    return _('%s() (in module %s)') % (name, modname)
                else:
                    return '%s()' % name
            if modname and add_modules:
                return _('%s() (%s.%s method)') % (methname, modname, clsname)
            else:
                return _('%s() (%s method)') % (methname, clsname)
        elif self.objtype == 'staticmethod':
            try:
                clsname, methname = name.rsplit('.', 1)
            except ValueError:
                if modname:
                    return _('%s() (in module %s)') % (name, modname)
                else:
                    return '%s()' % name
            if modname and add_modules:
                return _('%s() (%s.%s static method)') % (methname, modname,
                                                          clsname)
            else:
                return _('%s() (%s static method)') % (methname, clsname)
        elif self.objtype == 'classmethod':
            try:
                clsname, methname = name.rsplit('.', 1)
            except ValueError:
                if modname:
                    return _('%s() (in module %s)') % (name, modname)
                else:
                    return '%s()' % name
            if modname:
                return _('%s() (%s.%s class method)') % (methname, modname,
                                                         clsname)
            else:
                return _('%s() (%s class method)') % (methname, clsname)
        elif self.objtype == 'attribute':
            try:
                clsname, attrname = name.rsplit('.', 1)
            except ValueError:
                if modname:
                    return _('%s (in module %s)') % (name, modname)
                else:
                    return name
            if modname and add_modules:
                return _('%s (%s.%s attribute)') % (attrname, modname, clsname)
            else:
                return _('%s (%s attribute)') % (attrname, clsname)
        else:
            return ''

    def before_content(self):
        TCPIPObject.before_content(self)
        lastname = self.names and self.names[-1][1]
        if lastname and not self.env.temp_data.get('tcpip:class'):
            self.env.temp_data['tcpip:class'] = lastname.strip('.')
            self.clsname_set = True


class TCPIPModule(Directive):
    """
    Directive to mark description of a new module.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'platform': lambda x: x,
        'synopsis': lambda x: x,
        'noindex': directives.flag,
        'deprecated': directives.flag,
    }

    def run(self):
        env = self.state.document.settings.env
        modname = self.arguments[0].strip()
        noindex = 'noindex' in self.options
        env.temp_data['tcpip:module'] = modname
        env.domaindata['tcpip']['modules'][modname] = \
            (env.docname, self.options.get('synopsis', ''),
             self.options.get('platform', ''), 'deprecated' in self.options)
        targetnode = nodes.target('', '', ids=['module-' + modname], ismod=True)
        self.state.document.note_explicit_target(targetnode)
        ret = [targetnode]
        # XXX this behavior of the module directive is a mess...
        if 'platform' in self.options:
            platform = self.options['platform']
            node = nodes.paragraph()
            node += nodes.emphasis('', _('Platforms: '))
            node += nodes.Text(platform, platform)
            ret.append(node)
        # the synopsis isn't printed; in fact, it is only used in the
        # modindex currently
        if not noindex:
            indextext = _('%s (module)') % modname
            inode = addnodes.index(entries=[('single', indextext,
                                             'module-' + modname, modname, 'foobar')])
            ret.append(inode)
        return ret


class TCPIPCurrentModule(Directive):
    """
    This directive is just to tell Sphinx that we're documenting
    stuff in module foo, but links to module foo won't lead here.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        env = self.state.document.settings.env
        modname = self.arguments[0].strip()
        if modname == 'None':
            env.temp_data['tcpip:module'] = None
        else:
            env.temp_data['tcpip:module'] = modname
        return []


class TCPIPXRefRole(XRefRole):
    def _fix_parens(self, env, has_explicit_title, title, target):
        if not has_explicit_title:
            if title.endswith('()'):
                # remove parentheses
                title = title[:-2]
            if env.config.add_function_parentheses:
                # add them back to all occurrences if configured
                #title += '()' # Matthias: dont add them back
                pass
        # remove parentheses from the target too
        if target.endswith('()'):
            target = target[:-2]
        return title, target
        
    def process_link(self, env, refnode, has_explicit_title, title, target):
        refnode['tcpip:module'] = env.temp_data.get('tcpip:module')
        refnode['tcpip:class'] = env.temp_data.get('tcpip:class')
        if not has_explicit_title:
            title = title.lstrip('.')   # only has a meaning for the target
            target = target.lstrip('~') # only has a meaning for the title
            # if the first character is a tilde, don't display the module/class
            # parts of the contents
            if title[0:1] == '~':
                title = title[1:]
                dot = title.rfind('.')
                if dot != -1:
                    title = title[dot+1:]
        # if the first character is a dot, search more specific namespaces first
        # else search builtins first
        if target[0:1] == '.':
            target = target[1:]
            refnode['refspecific'] = True
        return title, target


class TCPIPModuleIndex(Index):
    """
    Index subclass to provide the TCP/IP module index.
    """

    name = 'modindex'
    localname = _('TCP/IP Module Index')
    shortname = _('modules')

    def generate(self, docnames=None):
        content = {}
        # list of prefixes to ignore
        ignores = self.domain.env.config['modindex_common_prefix']
        ignores = sorted(ignores, key=len, reverse=True)
        # list of all modules, sorted by module name
        modules = sorted(self.domain.data['modules'].items(),
                         key=lambda x: x[0].lower())
        # sort out collapsable modules
        prev_modname = ''
        num_toplevels = 0
        for modname, (docname, synopsis, platforms, deprecated) in modules:
            if docnames and docname not in docnames:
                continue

            for ignore in ignores:
                if modname.startswith(ignore):
                    modname = modname[len(ignore):]
                    stripped = ignore
                    break
            else:
                stripped = ''

            # we stripped the whole module name?
            if not modname:
                modname, stripped = stripped, ''

            entries = content.setdefault(modname[0].lower(), [])

            package = modname.split('.')[0]
            if package != modname:
                # it's a submodule
                if prev_modname == package:
                    # first submodule - make parent a group head
                    entries[-1][1] = 1
                elif not prev_modname.startswith(package):
                    # submodule without parent in list, add dummy entry
                    entries.append([stripped + package, 1, '', '', '', '', ''])
                subtype = 2
            else:
                num_toplevels += 1
                subtype = 0

            qualifier = deprecated and _('Deprecated') or ''
            entries.append([stripped + modname, subtype, docname,
                            'module-' + stripped + modname, platforms,
                            qualifier, synopsis])
            prev_modname = modname

        # apply heuristics when to collapse modindex at page load:
        # only collapse if number of toplevel modules is larger than
        # number of submodules
        collapse = len(modules) - num_toplevels < num_toplevels

        # sort by first letter
        content = sorted(content.items())

        return content, collapse


class TCPIPDomain(Domain):
    """TCP/IP language domain."""
    name = 'tcpip'
    label = 'TCP/IP'
    object_types = {
        'function':     ObjType(_('function'),      'func', 'obj'),
        'data':         ObjType(_('data'),          'data', 'obj'),
        'class':        ObjType(_('class'),         'class', 'obj'),
        'exception':    ObjType(_('exception'),     'exc', 'obj'),
        'method':       ObjType(_('method'),        'meth', 'obj'),
        'classmethod':  ObjType(_('class method'),  'meth', 'obj'),
        'staticmethod': ObjType(_('static method'), 'meth', 'obj'),
        'attribute':    ObjType(_('attribute'),     'attr', 'obj'),
        'module':       ObjType(_('module'),        'mod', 'obj'),
    }

    directives = {
        'function':      TCPIPModulelevel,
        'data':          TCPIPModulelevel,
        'class':         TCPIPClasslike,
        'exception':     TCPIPClasslike,
        'method':        TCPIPClassmember,
        'classmethod':   TCPIPClassmember,
        'staticmethod':  TCPIPClassmember,
        'attribute':     TCPIPClassmember,
        'module':        TCPIPModule,
        'currentmodule': TCPIPCurrentModule,
    }
    roles = {
        'data':  TCPIPXRefRole(),
        'exc':   TCPIPXRefRole(),
        'func':  TCPIPXRefRole(fix_parens=True),
        'class': TCPIPXRefRole(),
        'const': TCPIPXRefRole(),
        'attr':  TCPIPXRefRole(),
        'meth':  TCPIPXRefRole(fix_parens=True),
        'mod':   TCPIPXRefRole(),
        'obj':   TCPIPXRefRole(),
    }
    initial_data = {
        'objects': {},  # fullname -> docname, objtype
        'modules': {},  # modname -> docname, synopsis, platform, deprecated
    }
    indices = [
        TCPIPModuleIndex,
    ]

    def clear_doc(self, docname):
        to_delete = [fullname for fullname, (fn, _) in self.data['objects'].items()
                     if fn == docname]
        for fullname in to_delete:
            del self.data['objects'][fullname]
        to_delete = [modname for modname, (fn, _, _, _) in self.data['modules'].items()
                     if fn == docname]
        for modname in to_delete:
            del self.data['modules'][modname]

    def find_obj(self, env, modname, classname, name, type, searchorder=0):
        """
        Find a TCP/IP object for "name", perhaps using the given module and/or
        classname.  Returns a list of (name, object entry) tuples.
        """
        # skip parens
        if name[-2:] == '()':
            name = name[:-2]

        if not name:
            return None, None

        objects = self.data['objects']
        matches = []

        newname = None
        if searchorder == 1:
            if modname and classname and \
                   modname + '.' + classname + '.' + name in objects:
                newname = modname + '.' + classname + '.' + name
            elif modname and modname + '.' + name in objects:
                newname = modname + '.' + name
            elif name in objects:
                newname = name
            else:
                # "fuzzy" searching mode
                searchname = '.' + name
                matches = [(name, objects[name]) for name in objects
                           if name.endswith(searchname)]
        else:
            if name in objects:
                newname = name
            elif classname and classname + '.' + name in objects:
                newname = classname + '.' + name
            elif modname and modname + '.' + name in objects:
                newname = modname + '.' + name
            elif modname and classname and \
                     modname + '.' + classname + '.' + name in objects:
                newname = modname + '.' + classname + '.' + name
            # special case: builtin exceptions have module "exceptions" set
            elif type == 'exc' and '.' not in name and \
                 'exceptions.' + name in objects:
                newname = 'exceptions.' + name
            # special case: object methods
            elif type in ('func', 'meth') and '.' not in name and \
                 'object.' + name in objects:
                newname = 'object.' + name
        if newname is not None:
            matches.append((newname, objects[newname]))
        return matches

    def resolve_xref(self, env, fromdocname, builder,
                     type, target, node, contnode):
        if (type == 'mod' or
            type == 'obj' and target in self.data['modules']):
            docname, synopsis, platform, deprecated = \
                self.data['modules'].get(target, ('','','', ''))
            if not docname:
                return None
            else:
                title = '%s%s%s' % ((platform and '(%s) ' % platform),
                                    synopsis,
                                    (deprecated and ' (deprecated)' or ''))
                return make_refnode(builder, fromdocname, docname,
                                    'module-' + target, contnode, title)
        else:
            modname = node.get('tcpip:module')
            clsname = node.get('tcpip:class')
            searchorder = node.hasattr('refspecific') and 1 or 0
            matches = self.find_obj(env, modname, clsname, target,
                                    type, searchorder)
            if not matches:
                return None
            elif len(matches) > 1:
                env.warn(fromdocname,
                         'more than one target found for cross-reference '
                         '%r: %s' % (target,
                                     ', '.join(match[0] for match in matches)),
                         node.line)
            name, obj = matches[0]
            return make_refnode(builder, fromdocname, obj[0], name,
                                contnode, name)

    def get_objects(self):
        for modname, info in self.data['modules'].items():
            yield (modname, modname, 'module', info[0], 'module-' + modname, 0)
        for refname, (docname, type) in self.data['objects'].items():
            yield (refname, refname, type, docname, refname, 1)



def setup(app):
    Translatable.app_config = app.config
    app.add_domain(TCPIPDomain)
