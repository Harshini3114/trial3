A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Define a function to perform matrix multiplication
def matrix_mult(X, Y):
    result = [[0, 0], [0, 0]]
    
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    
    return result
