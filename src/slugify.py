# -*- coding: utf-8 -*-

"""A generic slugifier utility (currently only for Latin-based scripts)."""

import re
import unicodedata

__version__ = '0.0.1'


def slugify(string, space='-'):

    """
    Slugify a unicode string.

    Example:

        >>> slugify(u"Héllø Wörld")
        u"hello-world"

    """

    return re.sub(r'[-\s]+', space,
            unicode(
                re.sub(r'[^\w\s-]', '',
                    unicodedata.normalize('NFKD', string)
                    .encode('ascii', 'ignore'))
                .strip()
                .lower()))
