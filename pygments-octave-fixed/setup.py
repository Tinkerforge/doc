"""
Octave-fixed Pygments Lexer
"""
from setuptools import setup

setup(
    name='Octave-fixed Pygments Lexer',
    version='0.1.0',
    description="Octave-fixed for Pygments",
    author='Matthias Bolte',
    packages=['octave_fixed_lexer'],
    entry_points='''[pygments.lexers]
octavefixedlexer = octave_fixed_lexer:OctaveFixedLexer
'''
)
