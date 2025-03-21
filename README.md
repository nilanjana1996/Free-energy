# Free-energy
This repo is created for smooth and hassle-free plotting of Free energy landscape for protein-ligand molecular dynamics simulation result.

Free energy landscape (FEL) plot or 3D minima plot, and contour plots are one of the most important parameters to evaluate protein-ligand complex stability in molecular dynamics simulation study.

Once we have the MD run results, we can pre=process the data to generate input data for FEL plot.

Files we need: (1) trajectory.tpr, (2) trajectory_fit.xtc (reqrapped and re-centered using gmx trjconv)

Other pre-requisite: A recent version of GROMACS (tested using GROMACS 2024.2)

Steps for pre-processing:
$gmx covar -s trajectory.tpr -f trajectory.xtc -o eigenval.xvg -v eigenvec.trr -av average.pdb -mwa (select backbone(4))
$gmx anaeig -v eigenvec.trr -f tarjectory_fit.xtc -s trajectiry.tpr -proj proj.xvg -2d 2dproj.xvg -extr extreme.pdb -filt filtered.xtc -first 1 -last 2 (select backbone(4))
$gmx sham -f 2dproj.xvg -ls fel_sham.xpm -notim -ngrid 30 30 30

The generated fel_sham.xpm file contains input data for the plot.
The code will create an colored 3D overlay plot of the 3D minima, and the 2D contour plot at the bottom.
