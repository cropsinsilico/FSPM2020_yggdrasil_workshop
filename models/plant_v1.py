import os
import trimesh
import argparse
from yggdrasil import units
from yggdrasil.languages.Python.YggInterface import YggRpcClient

_dir = os.path.dirname(os.path.realpath(__file__))
light_rpc = YggRpcClient('light_plant')

def run(mesh, tmin, tmax, tstep):
    tmin = units.add_units(tmin, 'days')
    tmax = units.add_units(tmax, 'days')
    tstep = units.add_units(tstep, 'days')
    t = tmin
    while t < tmax:

        # Get light data by calling light model
        nvert = mesh.vertices.shape[0]
        light = np.zeros(nvert)
        for i in range(nvert):
            flag, ilight = light_rpc.call(mesh.vertices[i, 2])
            if not flag:
                raise Exception("Error calling model for vertex %d" % i)
            light[i] = ilight

        # Grow mesh
        scale = light * t / units.add_units(300.0, 'days')
        mesh.vertices[:, 2] += mesh.vertices[:, 2] * scale
        mesh.visual.vertex_colors = trimesh.visual.linear_color_map(light)

        # Save mesh for this timestep
        filename = os.path.join(_dir, f'../output/mesh_{t}.obj')
        with open(filename, 'w') as fd:
            mesh.export(fd, 'obj')

        # Advance time step
        t += tstep

    return mesh


# Parse command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Simulate plant growth over time.")
    parser.add_argument('tmin', help='Starting time (in days)', type=float)
    parser.add_argument('tmax', help='Ending time (in days)', type=float)
    parser.add_argument('tstep', help='Time step (in days)', type=float)
    parser.add_argument('--meshfile', help='Path to file where mesh is stored.',
                        default='../meshes/plants-2.obj')
    args = parser.parse_args()
    mesh = trimesh.load_mesh(args.meshfile)
    run(mesh, args.tmin, args.tmax, args.tstep)
