# Author : Shibu Meher
# Email : shibumeher@iisc.ac.in
# Date Modified : 10th June 2023

import numpy as np

def has_inversion(n_rotations):
    """Returns true if the n_rotations list has 3x3 operation for inversion.

    Parameters
    ----------
    n_rotations : list of 3x3 matrices
        List of n rotation matrix (Point Group Symmetry)

    Returns
    -------
    bool
        True for if n_rotations has inversion operator.
    """

    inversion = -np.identity(3, dtype=int)
    return np.any([np.all(rotation == inversion) for rotation in n_rotations])


def write_dataset(filename, dataset):
    """Takes dataset and write it in a file beautifully.

    Check the following reference for details about various terms.
    Ref - https://spglib.readthedocs.io/en/latest/python-spglib.html

    Parameters
    ----------
    filename : str or os.path
        File path with filename where the symmetry dataset should be written
    dataset : dict
        Contains all the information to be written into the output file

    """

    lines = []
    lines.append(
        "Check the following reference for details about various terms. \nRef - https://spglib.readthedocs.io/en/latest/python-spglib.html"
    )
    lines.append("\n\nFile Read : " + str(dataset["filename_read"]) + "\n")
    lines.append("\n\nSpace Group Number : " + str(dataset["number"]) + "\n")
    lines.append("Point Group : " + str(dataset["pointgroup"]) + "\n")
    lines.append(
        "Space Group (International) : " + str(dataset["international"]) + "\n"
    )
    lines.append("Space Group (Schoenflies) : " + str(dataset["schoenflies"]) + "\n")
    lines.append("Has inversion symmetry : " + str(dataset["has_inversion"]) + "\n")
    lines.append("Symmetry Precision : " + str(dataset["tolerance"]) + "\n")
    lines.append("Angle Tolerance : " + str(dataset["angle_tolerance"]) + "\n")
    lines.append("Hall Number : " + str(dataset["hall_number"]) + "\n")
    lines.append("Hall Symbol : " + str(dataset["hall"]) + "\n")
    lines.append("Choice : " + str(dataset["choice"]) + "\n")
    lines.append("Transformation Matrix : \n" + str(dataset["transformation_matrix"]))
    lines.append("\n\nOrigin Shift : " + str(dataset["origin_shift"]))
    lines.append("\n\nRotations : \n" + str(dataset["rotations"]))
    lines.append("\n\nTranslations : \n" + str(dataset["translations"]))
    lines.append("\n\nWickoff Letters : \n" + str(dataset["wyckoffs"]))
    lines.append(
        "\n\nSite Symmetry Symbols : \n" + str(dataset["site_symmetry_symbols"])
    )
    lines.append(
        "\n\nCrystallographic Orbits : \n" + str(dataset["crystallographic_orbits"])
    )
    lines.append("\n\nEquivalent Atoms : \n" + str(dataset["equivalent_atoms"]))
    lines.append("\n\nPrimitive Lattice : \n" + str(dataset["primitive_lattice"]))
    lines.append("\n\nMapping to Primitive : \n" + str(dataset["mapping_to_primitive"]))
    lines.append("\n\nStandard Lattice : \n" + str(dataset["std_lattice"]))
    lines.append("\n\nStandard Positions : \n" + str(dataset["std_positions"]))
    lines.append(
        "\n\nStandard Rotation Matrix : \n" + str(dataset["std_rotation_matrix"])
    )
    lines.append(
        "\n\nStandard Mapping to Primitive : \n"
        + str(dataset["std_mapping_to_primitive"])
    )

    with open(filename, "w") as f:
        f.writelines(lines)