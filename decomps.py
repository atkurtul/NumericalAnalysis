import numpy as np

def mby_swap(mat, i, order):
	def swap(x, y):
		return y, x
	if np.isclose(mat[i][i], np.finfo('f').eps):
		for j in range(i, 3):
			if not np.isclose(mat[j][i], np.finfo('f').eps):
				mat[j], mat[i] = swap(mat[i], mat[j])
				order[j], order[i] = swap(order[i], order[j])
				break
	return mat, order

def Gauss(A, b):
	A = np.append(A, np.reshape([b], (3, 1)), axis=1)
	order = np.arange(start=0, stop=3, step=1)
	for i in range(3):
		A, order = mby_swap(A, i, order)
		A[i] /= A[i][i]
		for j in range(i + 1, 3):
			A[j] -=  A[i] * A[j][i]
	for i in range(3):
		for j in range(i + 1, 3):
			A[i] -= A[j] * A[i][j]
	re = np.zeros(3)
	for i, x in zip(order, A[:,3]):
		re[i] = x
	return re

def dot(a, b):
	acc = 0
	for a, b in zip(a, b):
		acc += a * b
	return acc

def solveLU(L, U, b):
	y, x = np.zeros(3), np.zeros(3)
	for i, j in zip(range(3), range(2, -1, -1)):
		y[i] = (b[i] - dot(y[:i+1], L[i][:i+1])) / L[i][i]
	for i in range(2, -1, -1):
		x[i] = (y[i] - dot(x[-i:], U[i][-i:])) / U[i][i]
	return x

def Dolittle(A, b):
	L, U = np.zeros((3, 3)),  np.zeros((3, 3))
	U[0] = A[0]
	L[:,0] = A[:, 0] / A[0,0]
	for i in range(1, 3):
		for j in range(i, 3):
			U[i, j] = A[i, j] - dot(L[i], U[:,j])
			L[j, i] = (A[j, i] - dot(L[j], U[:,i])) / U[i, i]
	return solveLU(L, U, b)

def Cholesky(A, b):
	L = np.zeros((3,3))
	for i in range(3):
		L[i,i] = np.sqrt(A[i,i] - dot(L[i, :i], L[i, :i]))
		for j in range(i + 1, 3):
			L[j,i] = (A[j,i] - dot(L[i, :j], L[j,:j]))/L[i,i]
	return solveLU(L, np.transpose(L), b)

gauss = np.array(	
	[
		[2, -3, -1],
		[3, 2, -5], 
		[2, 4, -1]
	], dtype='f')
np.array([3, -9, -5])

dolittle = np.array(
	[
		[ 2.34,  -4.10,  1.78], 
		[-1.98,   3.47, -2.22], 
		[ 2.36,  -15.17, 6.18]
	], dtype='f')

choleski = np.array(
	[
		[1, 1, 1],
		[1, 2, 2],
		[1, 2, 3],
	], dtype='f')

print("Gauss solution for 1st matrix")
print(Gauss(gauss, np.array([3, -9, -5])))
print("Gauss solution for 2nd matrix")
print(Gauss(dolittle, np.array([0.02, -0.73, -6.63])))
print("Gauss solution for 3rd matrix")
print(Gauss(choleski, np.array([1, 1.5, 3])))

print("\nDolittle solution for 1st matrix")
print(Dolittle(gauss, np.array([3, -9, -5])))
print("Dolittle solution for 2nd matrix")
print(Dolittle(dolittle, np.array([0.02, -0.73, -6.63])))
print("Dolittle solution for 3rd matrix")
print(Dolittle(choleski, np.array([1, 1.5, 3])))

print("\nCholesky solution for 3rd matrix.\nThis solution will only work on appropriate matrices.")
print(Cholesky(choleski, np.array([1, 1.5, 3])))