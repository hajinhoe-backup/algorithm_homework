import random
import time
import TSP_DP
import TSP_BS


def random_matrix(n):  # it will generate a matrix n x n and diagonal is 0.
    matrix = [[0 for cor in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = random.random()
    return matrix


print("Above is test case!---------------------------------------")
matrix = random_matrix(int(input("What is your wnat size of matrix? ")))
start_time = time.time()
TSP_DP.TSP_DP(matrix)
end_time = time.time()
print("DP version : ", float(end_time - start_time))
start_time = time.time()
TSP_BS.TSP_BS(matrix)
end_time = time.time()
print("BS version : ", end_time - start_time)
for i in range(10):
    matrix = random_matrix(15)
    TSP_BS.TSP_BS(matrix)