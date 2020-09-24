import inspect
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter


def print_python_source(x):
    print(highlight(inspect.getsource(x), PythonLexer(),
                    Terminal256Formatter()))
