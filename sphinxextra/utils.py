# -*- coding: utf-8 -*-

from packaging.version import Version

import sphinx

def fixup_index_entry(entry):
    sphinx_version = Version(sphinx.__version__)

    if sphinx_version < Version('1.5.0'):
        # Sphinx < 1.5: 4-element tuple (type, value, target, main)
        return entry[:4] if len(entry) > 4 else entry
    else:
        # Sphinx >= 1.5: 5-element tuple (type, value, target, main, category_key)
        if len(entry) == 4:
            return entry + (None,)
        elif len(entry) == 5:
            return entry
        else:
            # Entry has more than 5 elements, truncate to 5
            return entry[:5]
