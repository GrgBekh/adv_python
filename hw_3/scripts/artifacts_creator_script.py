import numpy as np
import sys
from numpy.lib.mixins import NDArrayOperatorsMixin
sys.path.append('..')
from utils.MatrixModule import Matrix
from utils.MixinMatrixModule import MixinMatrix
from utils.MatrixModuleWithHash import HashableMatrix

np.random.seed(0)

A_gen = np.random.randint(0, 10, (10, 10)).tolist()
B_gen = np.random.randint(0, 10, (10, 10)).tolist()

A = Matrix(A_gen)
B = Matrix(B_gen)

matrix_sum = A + B
matrix_hdmrd = A * B
matrix_mul = A @ B

np.savetxt('../artifacts/3.1/matrix_sum.txt', np.array(matrix_sum.data), fmt='%d', delimiter=",")
np.savetxt('../artifacts/3.1/matrix_hdmrd.txt', np.array(matrix_hdmrd.data), fmt='%d', delimiter=",")
np.savetxt('../artifacts/3.1/matrix_mul.txt', np.array(matrix_mul.data), fmt='%d', delimiter=",")

A = MixinMatrix(A_gen)
B = MixinMatrix(B_gen)

matrix_sum = A + B
matrix_hdmrd = A * B
matrix_mul = A @ B

matrix_sum.save('../artifacts/3.2/matrix_sum.txt')
matrix_hdmrd.save('../artifacts/3.2/matrix_hdmrd.txt')
matrix_mul.save('../artifacts/3.2/matrix_mul.txt')

A =  [[1, 2], [3, 4]]
B =  [[1, 2], [7, 13]]
C =   [[17, 18], [19, 4]]
D = B

A = HashableMatrix(A)
B = HashableMatrix(B)
C = HashableMatrix(C)
D = HashableMatrix(D)

mat_sum = A + B
mat_hdmr_mul =  A * B
mat_mul =  A @ B
AB = A@B
CD = C@D

np.savetxt('../artifacts/3.3/A.txt', np.array(A.data), fmt='%d', delimiter=",")
np.savetxt('../artifacts/3.3/B.txt', np.array(B.data), fmt='%d', delimiter=",")
np.savetxt('../artifacts/3.3/C.txt', np.array(C.data), fmt='%d', delimiter=",")
np.savetxt('../artifacts/3.3/D.txt', np.array(D.data), fmt='%d', delimiter=",")
np.savetxt('../artifacts/3.3/AB.txt', np.array(AB.data), fmt='%d', delimiter=",")
np.savetxt('../artifacts/3.3/CD.txt', np.array(CD.data), fmt='%d', delimiter=",")


hashes_vals = {'A' : hash(A), 'B': hash(B), 'C' : hash(C), 'D': hash(D), 'AB' : hash(A@B), 'CD': hash(C@D)}

with open('../artifacts/3.3/hash.txt', 'w') as f:
    for matrix in hashes_vals.keys():
        f.write(f'hash({matrix}) = {hashes_vals[matrix]}\n')