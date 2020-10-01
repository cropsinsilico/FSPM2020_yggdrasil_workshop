import os
import glob
import pickle
import inspect
import trimesh
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.data import YamlLexer
from pygments.formatters import Terminal256Formatter
from pygments.lexers.c_cpp import CLexer, CppLexer
from pygments.lexers.r import SLexer
from pygments.lexers.fortran import FortranLexer
import matplotlib.pyplot as plt


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


def display_last_timestep(with_light=False):
    last_mesh = sorted(glob.glob('output/mesh_*.obj'))[-1]
    mesh = trimesh.load_mesh(last_mesh)
    if with_light:
        last_light = sorted(glob.glob('output/light_*.pkl'))[-1]
        with open(last_light, 'rb') as fd:
            light = pickle.load(fd)
        mesh.visual.vertex_colors = trimesh.visual.interpolate(
            light/max(light))
    return mesh.show()


def plot_mass():
    from yggdrasil.communication.AsciiTableComm import AsciiTableComm
    fd = AsciiTableComm('mass', address='output/mass.txt', direction='recv',
                        as_array=True)
    flag, masses = fd.recv_dict()
    plt.plot(masses['time'], masses['root_mass'], label='root mass')
    plt.plot(masses['time'],
             masses['plant_mass'].to(masses['root_mass'].units),
             label='plant_mass')
    plt.plot(masses['time'],
             masses['total_mass'].to(masses['root_mass'].units),
             label='total_mass')
    plt.xlabel('time (%s)' % masses['time'].units)
    plt.ylabel('mass (%s)' % masses['root_mass'].units)
    plt.legend()
    return plt.show()
