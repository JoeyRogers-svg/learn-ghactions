#include <pybind11/pybind11.h>
#include "fast.cpp"

namespace py = pybind11;

PYBIND11_MODULE(fast_module, m) {
    m.doc() = "High performance C++ module";
    m.def("fast_add", &add, "Sum integers");
}