from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = cythonize([
    "./pkg/nlohmann/nlohmann.pyx"
], language_level="3", build_dir="build", language="c++")

extensions[0].include_dirs.append("./pkg/nlohmann")
extensions[0].name = "pkg.nlohmann"

setup(ext_modules=extensions)

