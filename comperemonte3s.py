import random
import time
import TSP_BS
import monte3
import monte3_2
import monte3_1
import monte3_3


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

matrix_n = input("What is your wnat size of matrix? ")
performing = input("The number of execution? ")
monte50_len = 0
monte50_node = 0
monte25_len = 0
monte25_node = 0
monte5_len = 0
monte5_node = 0
matrix = random_matrix(int(matrix_n))
bs_tot_node = TSP_BS.TSP_BS(matrix)
for i in range(int(performing)):
    (min_length, tot_node) = monte3_3.TSP_BS(matrix)
    monte50_len = monte50_len + min_length
    monte50_node = monte50_node + tot_node
    (min_length, tot_node) = monte3_2.TSP_BS(matrix)
    monte25_len = monte25_len + min_length
    monte25_node = monte25_node + tot_node
    (min_length, tot_node) = monte3_1.TSP_BS(matrix)
    monte5_len = monte5_len + min_length
    monte5_node = monte5_node + tot_node

print("BS node average : ", bs_tot_node)
print("monte50", monte50_len/ int(performing),monte50_node/int(performing))
print("monte25", monte25_len / int(performing),monte25_node/int(performing))
print("monte5", monte5_len / int(performing), monte5_node/int(performing))
