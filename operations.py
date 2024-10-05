import numpy as np
def add_matrices(A, B):
    return np.add(A, B)
def subtract_matrices(A, B):
    return np.subtract(A, B)
def multiply_matrices(A, B):
    return np.dot(A, B)
def divide_matrices_elementwise(A, B):
    return np.divide(A, B)
def trace_of_matrix(A):
    return np.trace(A)
def main():
    print("Matrix operations: Addition, Subtraction, Multiplication, Element-wise Division, Trace")
    matrix_A = np.array([[1, 2], [3, 4]])
    matrix_B = np.array([[5, 6], [7, 8]])
    print(f"Matrix A:\n{matrix_A}")
    print(f"Matrix B:\n{matrix_B}")
    print("\nAddition of A and B:")
    print(add_matrices(matrix_A, matrix_B))
    print("\nSubtraction of B from A:")
    print(subtract_matrices(matrix_A, matrix_B))
    print("\nMultiplication of A and B:")
    print(multiply_matrices(matrix_A, matrix_B))
    print("\nElement-wise Division of A by B:")
    print(divide_matrices_elementwise(matrix_A, matrix_B))
    print("\nTrace of Matrix A:")
    print(trace_of_matrix(matrix_A))
if __name__ == "__main__":
    main()
