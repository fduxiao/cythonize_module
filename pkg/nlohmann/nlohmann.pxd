cdef extern from "<nlohmann/json.hpp>" namespace "nlohmann":
    cdef cppclass json:
        pass

cdef extern from "interface.hpp":
    void set_nil(json &j)


cdef class Json:
    cdef json j
