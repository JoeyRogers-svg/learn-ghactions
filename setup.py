# setup.py
from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "fast_module.fast_module",  # module name inside package
        ["src/fast_module/bindings.cpp"],  # your binding source
        include_dirs=[pybind11.get_include()],
        language="c++"
    )
]

setup(
    name="fast-module-demo",
    version="0.0.1",
    packages=["fast_module"],
    ext_modules=ext_modules,
    zip_safe=False,
)