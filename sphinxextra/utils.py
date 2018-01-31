# -*- coding: utf-8 -*-

from distutils.version import LooseVersion

import sphinx

def fixup_index_entry(entry):
    if LooseVersion(sphinx.__version__) < LooseVersion('1.5.0'): # FIXME: exact version is unknown
        return entry

    return entry + (None,)
