#!/bin/sh
set -x
FILE_LIST="origcellrun.out origfacerun.out cellinplacerun.out faceinplacerun.out reggridbycellrun.out reggridbyfacesrun.out"
./clamr_gpuonly -n 1024 -t 100 -i 100 -l 2 -A "cell"                   >& origcellrun.out
./clamr_gpuonly -n 1024 -t 100 -i 100 -l 2 -A "face"                   >& origfacerun.out
./clamr_gpuonly -n 1024 -t 100 -i 100 -l 2 -A "cell-in-place"          >& cellinplacerun.out
./clamr_gpuonly -n 1024 -t 100 -i 100 -l 2 -A "face-in-place"          >& faceinplacerun.out
./clamr_gpuonly -n 1024 -t 100 -i 100 -l 2 -A "regular-grid"           >& reggridbycellrun.out
./clamr_gpuonly -n 1024 -t 100 -i 100 -l 2 -A "regular-grid-by-faces"  >& reggridbyfacesrun.out
fgrep "Total CPU" ${FILE_LIST} | sed 's/run.out:Profiling: Total CPU          time was/ Total CPU/' 
fgrep "state_timer_finite_difference" ${FILE_LIST} | sed 's/run.out:CPU:   state_timer_finite_difference/ finite_difference/'
fgrep "mesh_timer_bidir  " ${FILE_LIST} | sed 's/run.out:CPU:       mesh_timer_bidir  / mesh_timer_bidir/'

fgrep "Memory peak" ${FILE_LIST} | grep -v "in startup" | sed 's/run.out:Memory peak/ Memory_peak/'
#./clamr_cpuonly -A "regular-cell-by-faces" -t 100 -i 10 -l 2

