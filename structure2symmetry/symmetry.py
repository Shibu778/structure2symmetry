# Author : Shibu Meher
# Email : shibumeher@iisc.ac.in
# Date Modified : 10th June 2023

import click
import os
from spglib import get_symmetry_dataset, get_spacegroup
from ase.io import read
from .utils import *

@click.command()
@click.option(
    "--filepath",
    default="./POSCAR",
    help="File path absolute or relative including the filename",
)
@click.option("--tolerance", default=1e-5, help="spglib symmetry tolerance")
@click.option("--angle_tolerance", default=0.01, help="spglib angle tolerance")
@click.option(
    "--destination",
    default="./",
    help="Destination folder where the symmetry information will be written",
)
@click.option(
    "--savefile",
    default="symmetry.info",
    help="Name of the file where symmetry information will be written",
)
def struct2symm(
    filepath,
    tolerance,
    angle_tolerance,
    destination="./",
    savefile="symmetry.info",
):
    """Returns a dictionary containing symmetry information.

    It uses spglib to determine the symmetry and ase to read the structure file.

    Supported structure files same as mentioned in https://wiki.fysik.dtu.dk/ase/ase/io/io.html .

    Parameters
    ----------
    filepath : str
        Absolute or relative filepath of the structure file
    tolerance : float
        Spglib symmetry precission
    angle_tolerance : float
        spglib angle precission
    destination : str or os.path
        Destination folder where the symmetry information will be written
    savefile : str
        Name of the file where symmetry information will be written

    Returns
    -------
    dataset : dictionary
        It contains all the information returned by dataset from spglib.get_symmetry_dataset and
        another key with has_inversion telling whether the inversion center is present or not.
    """

    struct = read(filepath)

    lattice = struct.get_cell().array
    positions = struct.get_scaled_positions(wrap=False)
    numbers = struct.get_atomic_numbers()

    spgcell = (lattice, positions, numbers)

    dataset = get_symmetry_dataset(
        spgcell, symprec=tolerance, angle_tolerance=angle_tolerance
    )

    dataset["has_inversion"] = has_inversion(dataset["rotations"])
    spacegroup_schoen = get_spacegroup(
        spgcell, symprec=tolerance, angle_tolerance=angle_tolerance, symbol_type=1
    )
    dataset["schoenflies"] = spacegroup_schoen
    dataset["tolerance"] = tolerance
    dataset["angle_tolerance"] = angle_tolerance
    dataset["filename_read"] = filepath

    filename = os.path.join(destination, savefile)
    write_dataset(filename, dataset)

    print("Point Group Symmetry : ", dataset["pointgroup"])
    print("Space Group Symmetry (International)", dataset["international"])
    print("Space Group Symmetry (Schoenflies)", dataset["schoenflies"])

    return dataset


if __name__ == "__main__":
    # filepath = "../tests/POSCAR"
    filepath = "../tests/SiC.cif"
    destination = "../tests/"
    tolerance = 1e-5
    angle_tolerance = 0.01
    dataset = struct2symm(filepath, tolerance, angle_tolerance, destination=destination)
    # print(dataset)
