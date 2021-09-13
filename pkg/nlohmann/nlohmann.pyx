cdef class Json:
    def __init__(self, x=None):
        self.from_python(x)

    def from_python(self, x):
        if x is None:
            set_nil(self.j)
        else:
            raise NotImplementedError(type(x))
