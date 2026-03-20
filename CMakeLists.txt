cmake_minimum_required(VERSION 3.15)
project(fast_module)

find_package(pybind11 REQUIRED)

pybind11_add_module(fast_module src/fast_module/fast.cpp)