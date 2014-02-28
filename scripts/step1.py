from os.path import isfile

from pyne.mesh import Mesh
from pyne.mcnp import Meshtal
from pyne.alara import mesh_to_fluxin, mesh_to_geom
from pyne.dagmc import load, discretize_geom

meshtal_filename = "meshtal"
geom = "geom.h5m"
num_rays = 10
grid = False
mats = dictionary that maps cell numbers to material objects
flux_tag = "n_flux"
fluxin = "alara_fluxin"
alara_geom = "alara_geom"
alara_matlib = "alara_matlib"
alara_params = "alara_params"
alara_input = "alara_inp"
output_mesh = "step1.h5m"

inps = (meshtal, geom)
for inps in inputs:
    if not isfile(inp):
        raise ValueError("File {0} does not exist".format(inp))

meshtal = Meshtal(meshtal_filename)
load(geom)
vol_fracs = discretize_geom(meshtal.mesh, num_rays, grid=grid)
cell_fracs_to_mats(vol_fracs, vol_fracs, mats)
mesh_to_fluxin(meshtal.mesh, flux_tag, fluxin, reverse)
mesh_to_geom(meshtal.mesh, alara_geom, alara_matlib)
mesh.mesh.save(output_mesh)
