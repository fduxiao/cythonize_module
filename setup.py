from setuptools import setup
from Cython.Distutils import Extension
from Cython.Build import cythonize

extensions = cythonize([
    Extension(
        "pkg.nlohmann", 
        ["./pkg/nlohmann/nlohmann.pyx"], 
        language="c++",
        include_dirs=["./pkg/nlohmann/"]
    )
], language_level="3", build_dir="build")

setup(ext_modules=extensions)
