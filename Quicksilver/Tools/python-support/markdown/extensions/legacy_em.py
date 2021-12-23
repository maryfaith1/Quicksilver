'''
Legacy Em Extension for Python-Markdown
=======================================

This extention provides legacy behavior for _connected_words_.

Copyright 2015-2018 The Python Markdown Project

License: [BSD](https://opensource.org/licenses/bsd-license.php)

'''

from . import Extension
from ..inlinepatterns import UnderscoreProcessor, EmStrongItem, EM_STRONG2_RE, STRONG_EM2_RE
import re

# _emphasis_
EMPHASIS_RE = r'(_)([^_]+)\1'

# __strong__
STRONG_RE = r'(_{2})(.+?)\1'

# __strong_em___
STRONG_EM_RE = r'(_)\1(?!\1)([^_]+?)\1(?!\1)(.+?)\1{3}'


class LegacyUnderscoreProcessor(UnderscoreProcessor):
    """Emphasis processor for handling strong and em matches inside underscores."""

    PATTERNS = [
        EmStrongItem(re.compile(EM_STRONG2_RE, re.DOTALL | re.UNICODE), 'double', 'strong,em'),
        EmStrongItem(re.compile(STRONG_EM2_RE, re.DOTALL | re.UNICODE), 'double', 'em,strong'),
        EmStrongItem(re.compile(STRONG_EM_RE, re.DOTALL | re.UNICODE), 'double2', 'strong,em'),
        EmStrongItem(re.compile(STRONG_RE, re.DOTALL | re.UNICODE), 'single', 'strong'),
        EmStrongItem(re.compile(EMPHASIS_RE, re.DOTALL | re.UNICODE), 'single', 'em')
    ]


class LegacyEmExtension(Extension):
    """ Add legacy_em extension to Markdown class."""

    def extendMarkdown(self, md):
        """ Modify inline patterns. """
        md.inlinePatterns.register(LegacyUnderscoreProcessor(r'_'), 'em_strong2', 50)


def makeExtension(**kwargs):  # pragma: no cover
    """ Return an instance of the LegacyEmExtension """
    return LegacyEmExtension(**kwargs)
