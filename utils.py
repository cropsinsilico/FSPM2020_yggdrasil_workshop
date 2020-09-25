import inspect
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.data import YamlLexer
from pygments.formatters import Terminal256Formatter


def print_python_source(x):
    print(highlight(inspect.getsource(x), PythonLexer(),
                    Terminal256Formatter()))


def print_yaml(fname):
    with open(fname, 'r') as fd:
        lines = fd.read()
    print(highlight(lines, YamlLexer(), Terminal256Formatter()))
