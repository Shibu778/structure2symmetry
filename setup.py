from setuptools import setup, find_packages

from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="structure2symmetry",
    version="0.1.0",
    description="Python library to obtain symmetry information from structure file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "struct2symm=structure2symmetry.symmetry:struct2symm",
        ],
    },
    url="",
    author="Shibu Meher",
    author_email="shibumeher@iisc.ac.in",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=["structure2symmetry"],
    include_package_data=True,
    install_requires=["click", "numpy", "spglib", "ase"],
)
