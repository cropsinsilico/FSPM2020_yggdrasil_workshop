import os
import inspect
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.data import YamlLexer
from pygments.formatters import Terminal256Formatter
from pygments.lexers.c_cpp import CLexer, CppLexer
from pygments.lexers.r import SLexer
from pygments.lexers.fortran import FortranLexer


ext_map = {'.py': 'python',
           '.c': 'c',
           '.cpp': 'c++',
           '.f90': 'fortran',
           '.R': 'R',
           '.yml': 'yaml'}
lexer_map = {'python': PythonLexer,
             'yaml': YamlLexer,
             'c': CLexer,
             'c++': CppLexer,
             'R': SLexer,
             'fortran': FortranLexer}


def print_source(fname, language=None):
    with open(fname, 'r') as fd:
        lines = fd.read()
    if language is None:
        language = ext_map[os.path.splitext(fname)[-1]]
    print(highlight(lines, lexer_map[language](), Terminal256Formatter()))


def print_python_source(x):
    print(highlight(inspect.getsource(x), PythonLexer(),
                    Terminal256Formatter()))


def print_yaml(fname):
    with open(fname, 'r') as fd:
        lines = fd.read()
    print(highlight(lines, YamlLexer(), Terminal256Formatter()))
