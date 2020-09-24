import pywavefront
import argparse


def run(mesh, tmin, tmax, tstep):
    t = tmin
    while t < tmax:

        # Grow mesh
        mesh.vertices[:, 2] += mesh.vertices[:, 2] * t / 300.0

        # Save mesh for this timestep
        filename = f'output/mesh_{t}.obj'
        with open(filename, 'w') as fd:
            mesh.export(fd, 'obj')

        # Advance time step
        t += tstep

    return mesh


# Parse command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Simulate plant growth over time.")
    parser.add_argument('tmin', help='Starting time (in days)')
    parser.add_argument('tmax', help='Ending time (in days)')
    parser.add_argument('tstep', help='Time step (in days)')
    parser.add_argument('--meshfile', help='Path to file where mesh is stored.',
                        default='../meshes/plants-2.obj')
    args = parser.parse_args()
    mesh = trimesh.load_mesh(args.meshfile)
    run(mesh, args.tmin, args.tmax, args.tstep)
