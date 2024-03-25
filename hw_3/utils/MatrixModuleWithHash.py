class HashMixin:
    """
    Самый простой хэш на свете, остаток от деления на некоторое число
    Будет всегда фиксированной длинны, удоволетворяет условию на хэш
    """
    def __hash__(self):
        return sum(sum(row) for row in self.data) % 16

class HashableMatrix(HashMixin):

    def __init__(self, list_of_lists):
        if len(list_of_lists) == 0:
            raise ValueError('Empty matrices are not supported')

        self.num_rows = len(list_of_lists)
        self.num_cols = len(list_of_lists[0])

        for i in range(len(list_of_lists)):
            if len(list_of_lists[i]) != self.num_cols:
                raise ValueError('Inconsistent length of rows of data')
        self.data = list_of_lists

    @property
    def shape(self):
        return (self.num_rows, self.num_cols)

    def __str__(self):
        out_str = ''
        for row in self.data:
            out_str += (str(row) + "\n")
        return out_str

    def __add__(self, other):
        if ((self.num_rows != other.num_rows) or (self.num_cols != other.num_cols)):
            raise ValueError('Shapes of matrices should be matching for this operation')
        else:
            out_matrix_data = []
            for i in range(self.num_rows):
                row = []
                for j in range(self.num_cols):
                    out_ij = self.data[i][j] + other.data[i][j]
                    row.append(out_ij)
                out_matrix_data.append(row)
            return (HashableMatrix(out_matrix_data))

    def __sub__(self, other):
        if ((self.num_rows != other.num_rows) or (self.num_cols != other.num_cols)):
            raise ValueError('Shapes of matrices should be matching for this operation')
        else:
            out_matrix_data = []
            for i in range(self.num_rows):
                row = []
                for j in range(self.num_cols):
                    out_ij = self.data[i][j] - other.data[i][j]
                    row.append(out_ij)
                out_matrix_data.append(row)
            return (HashableMatrix(out_matrix_data))

    def __truediv__(self, other):
        if ((self.num_rows != other.num_rows) or (self.num_cols != other.num_cols)):
            raise ValueError('Shapes of matrices should be matching for this operation')
        else:
            out_matrix_data = []
            for i in range(self.num_rows):
                row = []
                for j in range(self.num_cols):
                    if other.data[i][j] == 0:
                        raise ValueError(f'Zero division encountered at ({i + 1}, {j + 1})')
                    out_ij = self.data[i][j] / other.data[i][j]
                    row.append(out_ij)
                out_matrix_data.append(row)
            return (HashableMatrix(out_matrix_data))

    # hadamard product of matrices
    def __mul__(self, other):
        if ((self.num_rows != other.num_rows) or (self.num_cols != other.num_cols)):
            raise ValueError('Shapes of matrices should be matching for this operation')
        else:
            out_matrix_data = []
            for i in range(self.num_rows):
                row = []
                for j in range(self.num_cols):
                    out_ij = self.data[i][j] * other.data[i][j]
                    row.append(out_ij)
                out_matrix_data.append(row)
            return (HashableMatrix(out_matrix_data))

    # matrix multiplication of matrices
    def __matmul__(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError('Matrices should be congruent, like (m, n), (n, p) for any positive integers m, n, p')
        else:
            out_matrix_data = []
            for i in range(self.num_rows):
                row = []
                for j in range(other.num_cols):
                    out_ij = 0
                    for k in range(self.num_cols):
                        out_ij += self.data[i][k] * other.data[k][j]
                    row.append(out_ij)
                out_matrix_data.append(row)
            return (HashableMatrix(out_matrix_data))
