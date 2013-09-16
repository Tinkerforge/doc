            # display,            example,              uri,      filename, getting started
bindings = [('C/C++',             'C',                  'c',      'C',      {'en': 'http://www.cprogramming.com/',
                                                                             'de': 'http://www.cprogramming.com/'}), # http://www.c-howto.de/
            ('C#',                'C#',                 'csharp', 'CSharp', {'en': 'http://csharp.net-tutorials.com/',
                                                                             'de': 'http://csharp.net-tutorials.com/'}),
            ('Delphi',            'Delphi',             'delphi', 'Delphi', {'en': 'http://www.delphibasics.co.uk/',
                                                                             'de': 'http://www.delphi-treff.de/tutorials/grundlagen/'}),
            ('Java',              'Java',               'java',   'Java',   {'en': 'http://docs.oracle.com/javase/tutorial/',
                                                                             'de': 'http://docs.oracle.com/javase/tutorial/'}), # http://openbook.galileocomputing.de/javainsel/
            ('PHP',               'PHP',                'php',    'PHP',    {'en': 'http://www.php.net/manual/en/getting-started.php',
                                                                             'de': 'http://www.php.net/manual/de/getting-started.php'}),
            ('Python',            'Python',             'python', 'Python', {'en': 'http://www.python.org/about/gettingstarted/', # http://getpython3.com/diveintopython3/
                                                                             'de': 'http://www.python.org/about/gettingstarted/'}),
            ('Ruby',              'Ruby',               'ruby',   'Ruby',   {'en': 'http://www.ruby-lang.org/en/documentation/quickstart/',
                                                                             'de': 'http://www.ruby-lang.org/de/documentation/quickstart/'}),
            ('Shell',             'Shell',              'shell',  'Shell',  {'en': '',
                                                                             'de': ''}),
            ('Visual Basic .NET', 'Visual Basic .NET',  'vbnet',  'VBNET',  {'en': 'http://howtostartprogramming.com/vb-net/',
                                                                             'de': 'http://howtostartprogramming.com/vb-net/'})] # http://openbook.galileocomputing.de/vb_net/index.htm

binding_name = {
'en':
""":ref:`{0} <api_bindings_{1}>`""",
'de':
""":ref:`{0} <api_bindings_{1}>`"""
}

binding_names = {
'en':
"""
.. |bindings| replace:: {0}
""",
'de':
"""
.. |bindings| replace:: {0}
"""
}
