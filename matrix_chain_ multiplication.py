def matrix_chain_multiplication(p):
    n = len(p) - 1  # Number of matrices
    m = [[float('inf')]*n for _ in range(n)]

    for i in range(n):
        m[i][i] = 0

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                m[i][j] = min(m[i][j], cost)

    return m[0][n-1]

matrix_dimensions = [20, 5, 40, 55, 12, 30, 23]
total_scalar_multiplications = matrix_chain_multiplication(matrix_dimensions)

print("Total Scalar Multiplications:", total_scalar_multiplications)
