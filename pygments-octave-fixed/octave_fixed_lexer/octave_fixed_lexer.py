import re
from string import whitespace
from pygments.lexer import RegexLexer, bygroups, include, using, this
from pygments.token import *

class OctaveFixedLexer(RegexLexer):
    """
    For GNU Octave source code.
    Contributed by Ken Schutte <kschutte@csail.mit.edu>.
    Fixed for " used by Octave instead of '
    """
    name = 'OctaveFixed'
    aliases = ['octave_fixed']
    filenames = ['*.m']
    mimetypes = ['text/octave']

    #
    # These lists are generated automatically.
    # Run the following in bash shell:
    #
    # for f in elfun specfun elmat; do
    #   echo -n "$f = "
    #   matlab -nojvm -r "help $f;exit;" | perl -ne \
    #   'push(@c,$1) if /^    (\w+)\s+-/; END {print q{["}.join(q{","},@c).qq{"]\n};}'
    # done
    #
    # elfun: Elementary math functions
    # specfun: Special Math functions
    # elmat: Elementary matrices and matrix manipulation
    #
    # taken from Matlab version 7.4.0.336 (R2007a)
    #
    elfun = ["sin","sind","sinh","asin","asind","asinh","cos","cosd","cosh",
             "acos","acosd","acosh","tan","tand","tanh","atan","atand","atan2",
             "atanh","sec","secd","sech","asec","asecd","asech","csc","cscd",
             "csch","acsc","acscd","acsch","cot","cotd","coth","acot","acotd",
             "acoth","hypot","exp","expm1","log","log1p","log10","log2","pow2",
             "realpow","reallog","realsqrt","sqrt","nthroot","nextpow2","abs",
             "angle","complex","conj","imag","real","unwrap","isreal","cplxpair",
             "fix","floor","ceil","round","mod","rem","sign"]
    specfun = ["airy","besselj","bessely","besselh","besseli","besselk","beta",
               "betainc","betaln","ellipj","ellipke","erf","erfc","erfcx",
               "erfinv","expint","gamma","gammainc","gammaln","psi","legendre",
               "cross","dot","factor","isprime","primes","gcd","lcm","rat",
               "rats","perms","nchoosek","factorial","cart2sph","cart2pol",
               "pol2cart","sph2cart","hsv2rgb","rgb2hsv"]
    elmat = ["zeros","ones","eye","repmat","rand","randn","linspace","logspace",
             "freqspace","meshgrid","accumarray","size","length","ndims","numel",
             "disp","isempty","isequal","isequalwithequalnans","cat","reshape",
             "diag","blkdiag","tril","triu","fliplr","flipud","flipdim","rot90",
             "find","end","sub2ind","ind2sub","bsxfun","ndgrid","permute",
             "ipermute","shiftdim","circshift","squeeze","isscalar","isvector",
             "ans","eps","realmax","realmin","pi","i","inf","nan","isnan",
             "isinf","isfinite","j","why","compan","gallery","hadamard","hankel",
             "hilb","invhilb","magic","pascal","rosser","toeplitz","vander",
             "wilkinson"]

    tokens = {
        'root': [
            # line starting with '!' is sent as a system command.  not sure what
            # label to use...
            (r'^!.*', String.Other),
            (r'%.*$', Comment),
            (r'^\s*function', Keyword, 'deffunc'),

            # from 'iskeyword' on version 7.11 (R2010):
            (r'(break|case|catch|classdef|continue|else|elseif|end|enumerated|'
             r'events|for|function|global|if|methods|otherwise|parfor|'
             r'persistent|properties|return|spmd|switch|try|while)\b', Keyword),

            ("(" + "|".join(elfun+specfun+elmat) + r')\b',  Name.Builtin),

            # operators:
            (r'-|==|~=|<|>|<=|>=|&&|&|~|\|\|?', Operator),
            # operators requiring escape for re:
            (r'\.\*|\*|\+|\.\^|\.\\|\.\/|\/|\\', Operator),

            # punctuation:
            (r'\[|\]|\(|\)|\{|\}|:|@|\.|,', Punctuation),
            (r'=|:|;', Punctuation),

            # quote can be transpose, instead of string:
            # (not great, but handles common cases...)
            (r'(?<=[\w\)\]])\'', Operator),

            (r'(?<![\w\)\]])\"', String, 'string'),
            ('[a-zA-Z_][a-zA-Z0-9_]*', Name),
            (r'.', Text),
        ],
        'string': [
            (r'[^\"]*\"', String, '#pop')
        ],
        'deffunc': [
            (r'(\s*)(?:(.+)(\s*)(=)(\s*))?(.+)(\()(.*)(\))(\s*)',
             bygroups(Text.Whitespace, Text, Text.Whitespace, Punctuation,
                      Text.Whitespace, Name.Function, Punctuation, Text,
                      Punctuation, Text.Whitespace), '#pop'),
        ],
    }

    def analyse_text(text):
        if re.match(r'^\s*%', text, re.M): # comment
            return 0.9
        elif re.match(r'^!\w+', text, re.M): # system cmd
            return 0.9
        return 0.1
