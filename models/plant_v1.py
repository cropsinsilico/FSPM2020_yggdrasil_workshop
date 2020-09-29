import os
import trimesh
import argparse
import numpy as np
from yggdrasil import units
from yggdrasil.languages.Python.YggInterface import YggRpcClient, YggOutput

_dir = os.path.dirname(os.path.realpath(__file__))

def run(mesh, tmin, tmax, tstep):
    light_rpc = YggRpcClient('light_plant')
    light_out = YggOutput('light')
    tmin = units.add_units(tmin, 'days')
    tmax = units.add_units(tmax, 'days')
    tstep = units.add_units(tstep, 'days')
    t = tmin
    while t < tmax:

        # Get light data by calling light model
        flag, light = light_rpc.call(mesh.vertices[:, 2], t)
        if not flag:
            raise Exception("Error calling light model")
        
        # Grow mesh
        scale = 2.0 * light
        mesh.vertices[:, 2] += mesh.vertices[:, 2] * scale

        # Save mesh for this timestep
        suffix = '{:04.1f}'.format(units.get_data(t))
        filename_mesh = os.path.join(_dir, f'../output/mesh_{suffix}.obj')
        with open(filename_mesh, 'w') as fd:
            mesh.export(fd, 'obj')

        # Send light to output
        flag = light_out.send(light)
        if not flag:
            raise Exception("Error sending light to output")

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
