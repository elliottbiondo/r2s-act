# Modify and copy source.F90 file
python hide_source.py ../source_moab.F90

# Generate the .o files..
gfortran -c mcnp_placeholder.F90 -fbounds-check -g -pedantic

gfortran -c source.F90 -fbounds-check -g -fcray-pointer -I/filespace/groups/cnerg/opt/MOAB/opt-cubit-c12/include -lstdc++ -liMesh -L/filespace/groups/cnerg/opt/MOAB/opt-nocgm/lib -lMOAB -lhdf5 -lnetcdf 

# compile!
#gfortran test_source.F90 -o test_source   mcnp_placeholder.o source.o -fbounds-check -g -pedantic
# compile!
gfortran test_source.F90 -o test_source   -fcray-pointer mcnp_placeholder.o source.o -fbounds-check -g -liMesh -L/filespace/groups/cnerg/opt/MOAB/opt-nocgm/lib -I/filespace/groups/cnerg/opt/MOAB/opt-cubit-c12/include -lMOAB -lhdf5 -lnetcdf -lstdc++


# run unit tests
#./test_source

# cleanup
#rm *.o
#rm *.mod
rm test_source
rm source.F90
