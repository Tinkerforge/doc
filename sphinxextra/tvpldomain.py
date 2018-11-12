# -*- coding: utf-8 -*-
"""
    sphinx.domains.tvpl
    ~~~~~~~~~~~~~~~~~~~

    The TVPL domain.

    :copyright: Copyright 2007-2011 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
from sphinx.domains import Domain, ObjType, Index
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util.compat import Directive
from sphinx.util.docfields import Field, GroupedField, TypedField

from sphinxextra.utils import fixup_index_entry

trans = {
'en_US': {
    'Inputs': 'Inputs',
    'Output': 'Output'
    },
'de_DE': {
    'Inputs': u'Eingänge',
    'Output': 'Ausgabe'
    }
}

class Translatable:
    app_config = None

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return trans[self.app_config.language][self.key]


class desc_parameterlist(nodes.Part, nodes.Inline, nodes.TextElement):
    child_text_separator = ' '

def _pseudo_parse_arglist(signode, arglist):
    """"Parse" a list of arguments separated by commas.

    Arguments can have "optional" annotations given by enclosing them in
    brackets.  Currently, this will split at any comma, even if it's inside a
    string literal (e.g. default argument value).
    """
    paramlist = desc_parameterlist()
    stack = [paramlist]
    try:
        for argument in arglist.split(' '):
            argument = argument.strip()
            ends_open = ends_close = 0
            while argument.startswith('['):
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                argument = argument[1:].strip()
            while argument.startswith(']'):
                stack.pop()
                argument = argument[1:].strip()
            while argument.endswith(']'):
                ends_close += 1
                argument = argument[:-1].strip()
            while argument.endswith('['):
                ends_open += 1
                argument = argument[:-1].strip()
            if argument:
                stack[-1] += addnodes.desc_parameter(argument, argument)
            while ends_open:
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                ends_open -= 1
            while ends_close:
                stack.pop()
                ends_close -= 1
        if len(stack) != 1:
            raise IndexError
    except IndexError:
        # if there are too few or too many elements on the stack, just give up
        # and treat the whole argument list as one argument, discarding the
        # already partially populated paramlist node
        signode += addnodes.desc_annotation(' ', ' ')
        signode += desc_parameterlist()
        signode[-1] += addnodes.desc_parameter(arglist, arglist)
    else:
        signode += addnodes.desc_annotation(' ', ' ')
        signode += paramlist

class TVPLObject(ObjectDescription):
    """
    Description of a general TVPL object.
    """
    option_spec = {
        'noindex': directives.flag,
        'module': directives.unchanged,
    }

    doc_field_types = [
        TypedField('parameter', label=Translatable('Inputs'),
                   names=('param', 'parameter', 'arg', 'argument',
                          'keyword', 'kwarg', 'kwparam', 'request'),
                   typerolename='obj', typenames=('paramtype', 'type')),
        TypedField('returnvalue', label=Translatable('Output'),
                   names=('returns', 'return', 'response'),
                   typerolename='obj', typenames=('paramtype', 'type')),
        Field('noreturnvalue', label=Translatable('Output'), has_arg=False,
              names=('noreturn',)),
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
        s = sig.split(' ')

        if True:
            name_prefix = None
            name = None
            paramlist = None
            first = True

            for p in s:
                p = p.replace('_', ' ')

                if len(p) == 0:
                    continue

                if not first:
                    if paramlist is None:
                        signode += addnodes.desc_annotation(' ', ' ')
                else:
                    first = False

                if p.startswith('L'): # param
                    if paramlist is None:
                        paramlist = desc_parameterlist()

                    paramlist += addnodes.desc_parameter(p[1:], p[1:])
                else:
                    if paramlist is not None:
                        signode += paramlist
                        paramlist = None
                        signode += addnodes.desc_annotation(' ', ' ')

                    if p.startswith('S'): # sig_prefix
                        signode += addnodes.desc_annotation(p[1:] + ' ', p[1:] + ' ')
                    elif p.startswith('P'): # name_prefix
                        name_prefix = p[1:]
                        signode += addnodes.desc_addname(name_prefix, name_prefix)
                    elif p.startswith('N'): # name
                        name = p[1:]
                        np = name.split(' ')
                        for k in np[:-1]:
                            signode += addnodes.desc_name(k, k)
                            signode += addnodes.desc_annotation(' ', ' ')
                        signode += addnodes.desc_name(np[-1], np[-1])
                    elif p.startswith('A'): # annotation
                        signode += addnodes.desc_annotation(p[1:], p[1:])
                    elif p.startswith('R'): # returns
                        signode += addnodes.desc_returns(p[1:], p[1:])

            if paramlist is not None:
                signode += paramlist
                paramlist = None

            if name_prefix:
                classname = name_prefix.lstrip(' ')
                fullname = name + ' of ' + name_prefix
            else:
                classname = ''
                fullname = name

            modname = self.options.get('module', self.env.temp_data.get('tvpl:module'))
            signode['module'] = modname
            signode['class'] = classname
            signode['fullname'] = fullname

            return fullname, name_prefix

        m = tvpl_sig_re.match(sig)
        if m is None:
            print 'FAILED', sig
            raise ValueError
        sig_prefix, name_prefix, name, arglist = m.groups()

        arglist = arglist.strip()
        if len(arglist) == 0:
            arglist = None

        # determine module and class name (if applicable), as well as full name
        modname = self.options.get('module', self.env.temp_data.get('tvpl:module'))
        classname = self.env.temp_data.get('tvpl:class')
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
                classname = name_prefix.rstrip(' ')
                fullname = name_prefix + ' ' + name
            else:
                classname = ''
                fullname = name

        #print ">" + str(modname) + '<', ">" + classname + '<', ">" + fullname + '<'

        signode['module'] = modname
        signode['class'] = classname
        signode['fullname'] = fullname

        #sig_prefix = self.get_signature_prefix(sig)
        if sig_prefix:
            signode += addnodes.desc_annotation(sig_prefix, sig_prefix)

        if name_prefix:
            signode += addnodes.desc_addname(name_prefix, name_prefix)
        # exceptions are a special case, since they are documented in the
        # 'exceptions' module.
        elif add_module and self.env.config.add_module_names:
            modname = self.options.get(
                'module', self.env.temp_data.get('tvpl:module'))
            if modname and modname != 'exceptions':
                nodetext = modname + '.'
                signode += addnodes.desc_addname(nodetext, nodetext)

        if sig_prefix:
            signode += addnodes.desc_annotation(' <uid> ', ' <uid> ')
        else:
            signode += addnodes.desc_annotation(' ', ' ')

        signode += addnodes.desc_name(name, name)
        if not arglist:
            if self.needs_arglist():
                # for callables, add an empty parameter list
                signode += desc_parameterlist()
            #if retann:
            #    signode += addnodes.desc_returns(retann, retann)
            return fullname, name_prefix
        _pseudo_parse_arglist(signode, arglist)
        #if retann:
        #    signode += addnodes.desc_returns(retann, retann)
        return fullname, name_prefix

    def get_index_text(self, modname, name):
        """
        Return the text for the index entry of the object.
        """
        raise NotImplementedError('must be implemented in subclasses')

    def add_target_and_index(self, name_cls, sig, signode):
        modname = self.options.get(
            'module', self.env.temp_data.get('tvpl:module'))
        fullname = (modname and modname + '.' or '') + name_cls[0]
        # note target
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['tvpl']['objects']
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
            self.env.temp_data['tvpl:class'] = None


class TVPLModulelevel(TVPLObject):
    """
    Description of an object on module level (functions, data).
    """

    def needs_arglist(self):
        return self.objtype == 'function'

    def get_index_text(self, modname, name_cls):
        if self.objtype == 'function':
            if not modname:
                return _('%s() (built-in function)') % name_cls[0]
            return _('%s() (in module %s)') % (name_cls[0], modname)
        elif self.objtype == 'data':
            if not modname:
                return _('%s (built-in variable)') % name_cls[0]
            return _('%s (in module %s)') % (name_cls[0], modname)
        else:
            return ''


class TVPLClasslike(TVPLObject):
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
        TVPLObject.before_content(self)
        if self.names:
            self.env.temp_data['tvpl:class'] = self.names[0][0]
            self.clsname_set = True


class TVPLClassmember(TVPLObject):
    """
    Description of a class member (methods, attributes).
    """

    def needs_arglist(self):
        return self.objtype.endswith('method')

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
        TVPLObject.before_content(self)
        lastname = self.names and self.names[-1][1]
        if lastname and not self.env.temp_data.get('tvpl:class'):
            self.env.temp_data['tvpl:class'] = lastname.strip('.')
            self.clsname_set = True


class TVPLModule(Directive):
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
        env.temp_data['tvpl:module'] = modname
        env.domaindata['tvpl']['modules'][modname] = \
            (env.docname, self.options.get('synopsis', ''),
             self.options.get('platform', ''), 'deprecated' in self.options)
        # make a duplicate entry in 'objects' to facilitate searching for the
        # module in TVPLDomain.find_obj()
        env.domaindata['tvpl']['objects'][modname] = (env.docname, 'module')
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


class TVPLCurrentModule(Directive):
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
            env.temp_data['tvpl:module'] = None
        else:
            env.temp_data['tvpl:module'] = modname
        return []


class TVPLXRefRole(XRefRole):
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
        refnode['tvpl:module'] = env.temp_data.get('tvpl:module')
        refnode['tvpl:class'] = env.temp_data.get('tvpl:class')
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


class TVPLModuleIndex(Index):
    """
    Index subclass to provide the TVPL module index.
    """

    name = 'modindex'
    localname = l_('TVPL Module Index')
    shortname = l_('modules')

    def generate(self, docnames=None):
        content = {}
        # list of prefixes to ignore
        ignores = self.domain.env.config['modindex_common_prefix']
        ignores = sorted(ignores, key=len, reverse=True)
        # list of all modules, sorted by module name
        modules = sorted(self.domain.data['modules'].iteritems(),
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
        content = sorted(content.iteritems())

        return content, collapse


class TVPLDomain(Domain):
    """TVPL language domain."""
    name = 'tvpl'
    label = 'TVPL'
    object_types = {
        'function':     ObjType(l_('function'),      'func', 'obj'),
        'data':         ObjType(l_('data'),          'data', 'obj'),
        'class':        ObjType(l_('class'),         'class', 'obj'),
        'exception':    ObjType(l_('exception'),     'exc', 'obj'),
        'method':       ObjType(l_('method'),        'meth', 'obj'),
        'classmethod':  ObjType(l_('class method'),  'meth', 'obj'),
        'staticmethod': ObjType(l_('static method'), 'meth', 'obj'),
        'attribute':    ObjType(l_('attribute'),     'attr', 'obj'),
        'module':       ObjType(l_('module'),        'mod', 'obj'),
    }

    directives = {
        'function':      TVPLModulelevel,
        'data':          TVPLModulelevel,
        'class':         TVPLClasslike,
        'exception':     TVPLClasslike,
        'method':        TVPLClassmember,
        'classmethod':   TVPLClassmember,
        'staticmethod':  TVPLClassmember,
        'attribute':     TVPLClassmember,
        'module':        TVPLModule,
        'currentmodule': TVPLCurrentModule,
    }
    roles = {
        'data':  TVPLXRefRole(),
        'exc':   TVPLXRefRole(),
        'func':  TVPLXRefRole(fix_parens=True),
        'class': TVPLXRefRole(),
        'const': TVPLXRefRole(),
        'attr':  TVPLXRefRole(),
        'meth':  TVPLXRefRole(fix_parens=True),
        'mod':   TVPLXRefRole(),
        'obj':   TVPLXRefRole(),
    }
    initial_data = {
        'objects': {},  # fullname -> docname, objtype
        'modules': {},  # modname -> docname, synopsis, platform, deprecated
    }
    indices = [
        TVPLModuleIndex,
    ]

    def clear_doc(self, docname):
        for fullname, (fn, _) in self.data['objects'].items():
            if fn == docname:
                del self.data['objects'][fullname]
        for modname, (fn, _, _, _) in self.data['modules'].items():
            if fn == docname:
                del self.data['modules'][modname]

    def find_obj(self, env, modname, classname, name, type, searchmode=0):
        """
        Find a TVPL object for "name", perhaps using the given module and/or
        classname.  Returns a list of (name, object entry) tuples.
        """
        # skip parens
        if name[-2:] == '()':
            name = name[:-2]

        if not name:
            return []

        objects = self.data['objects']
        matches = []

        newname = None
        if searchmode == 1:
            objtypes = self.objtypes_for_role(type)
            if modname and classname:
                fullname = modname + '.' + classname + '.' + name
                if fullname in objects and objects[fullname][1] in objtypes:
                    newname = fullname
            if not newname:
                if modname and modname + '.' + name in objects and \
                   objects[modname + '.' + name][1] in objtypes:
                    newname = modname + '.' + name
                elif name in objects and objects[name][1] in objtypes:
                    newname = name
                else:
                    # "fuzzy" searching mode
                    searchname = '.' + name
                    matches = [(name, objects[name]) for name in objects
                               if name.endswith(searchname)
                               and objects[name][1] in objtypes]
        else:
            # NOTE: searching for exact match, object type is not considered
            if name in objects:
                newname = name
            elif type == 'mod':
                # only exact matches allowed for modules
                return []
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
        modname = node.get('tvpl:module')
        clsname = node.get('tvpl:class')
        searchmode = node.hasattr('refspecific') and 1 or 0
        matches = self.find_obj(env, modname, clsname, target,
                                type, searchmode)
        if not matches:
            return None
        elif len(matches) > 1:
            env.warn(fromdocname,
                     'more than one target found for cross-reference '
                     '%r: %s' % (target,
                                 ', '.join(match[0] for match in matches)),
                     node.line)
        name, obj = matches[0]

        if obj[1] == 'module':
            # get additional info for modules
            docname, synopsis, platform, deprecated = self.data['modules'][name]
            assert docname == obj[0]
            title = name
            if synopsis:
                title += ': ' + synopsis
            if deprecated:
                title += _(' (deprecated)')
            if platform:
                title += ' (' + platform + ')'
            return make_refnode(builder, fromdocname, docname,
                                'module-' + name, contnode, title)
        else:
            return make_refnode(builder, fromdocname, obj[0], name,
                                contnode, name)

    def get_objects(self):
        for modname, info in self.data['modules'].iteritems():
            yield (modname, modname, 'module', info[0], 'module-' + modname, 0)
        for refname, (docname, type) in self.data['objects'].iteritems():
            yield (refname, refname, type, docname, refname, 1)




def setup(app):
    Translatable.app_config = app.config
    app.add_domain(TVPLDomain)
