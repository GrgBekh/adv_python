import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class StrMixin:
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


class SaveLoadMixin:
    def save(self, filename):
        np.savetxt(filename, self.data, fmt='%d', delimiter=",")

    @classmethod
    def load(cls, filename):
        data = np.loadtxt(filename, dtype=float).tolist()
        return cls(data)


class DataAccessMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        if len(value) == 0:
            raise ValueError('Empty matrices are not supported')
        if len(value[0]) == 0:
            raise ValueError('Empty columns are not supported')
        self.num_rows = len(value)
        self.num_cols = len(value[0])


class MixinMatrix(NDArrayOperatorsMixin, StrMixin, SaveLoadMixin, DataAccessMixin):
    def __init__(self, list_of_lists):
        if not list_of_lists:
            raise ValueError('Empty matrices are not supported')
        self.data = list_of_lists

    def __array__(self):
        return self.data

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        new_inputs = []
        for input_ in inputs:
            if isinstance(input_, MixinMatrix):
                new_inputs.append(input_.data)
            else:
                new_inputs.append(input_)

        result = getattr(ufunc, method)(*new_inputs, **kwargs)

        if method == '__call__' and isinstance(result, np.ndarray):
            return MixinMatrix(result.tolist())
        else:
            return result