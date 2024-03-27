# structure2symmetry

This is a small python code, which uses Atomic Simulation Environment and spglib to determine the symmetry information from a structure file like POSCAR, CIF and many more supported by ase.io.read (refer to https://wiki.fysik.dtu.dk/ase/ase/io/io.html).

## Installation

Using `pip`, use the following command to install

`pip install structure2symmetry`

Using the source code, use the following set of command

```
git clone https://github.com/Shibu778/structure2symmetry.git
cd structure2symmetry
pip install -e .
```

## Use

You can use the following command line interface to get symmetry information from a structure file.

```
struct2symm --filepath "./SiC.cif" --tolerance 1e-6 --angle_tolerance 0.01 --destination "./" --savefile "data.info"
```
