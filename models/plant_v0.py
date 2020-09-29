import os
import trimesh
import argparse

_dir = os.path.dirname(os.path.realpath(__file__))

def run(mesh, tmin, tmax, tstep):
    t = tmin
    while t < tmax:

        # Grow mesh
        scale = t / 300.0
        mesh.vertices[:, 2] += mesh.vertices[:, 2] * scale

        # Save mesh for this timestep
        filename = os.path.join(_dir, f'../output/mesh_{t:03.1f}.obj')
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
