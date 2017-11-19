# This program will find out TSP by DP
# v start from 0
import copy


def subset(set):  # this will return subsets without empty set.
    set = copy.copy(set)
    subset = []
    def get_subset(set, index):
        if len(set) == 0:
            return
        elif index == len(set):
            subset.append(set)
            return
        get_subset(copy.copy(set), index + 1)
        set.pop(index)
        get_subset(copy.copy(set), index)
    get_subset(set, 0)
    return subset


def encode_city(set):  # if empty set return 0, and ser of [0, 3] return 9, and ....
    sum = 0
    if set:
        for i in set:
            sum = sum + 2**i
    return sum


def TSP_DP(W):
    n = len(W)

    D = [[0 for col in range(2**n)] for row in range(n)]
    P = [[0 for col in range(2**n)] for row in range(n)]

    V = []
    for i in range(0, n):
        V.append(i)
    V.remove(0)
    V_sub = subset(V)  # note not include 0

    for i in range(1, n):
        D[i][0] = W[i][0]
    for k in range(1, n - 1):
        for A in V_sub:
            if len(A) == k:  # all subsets A ~
                for i in V:  # V not include 0
                    if i not in A:
                        for j in A:
                            B = copy.deepcopy(A)  # note copy.deepcopy(A).remove(j) not work, remove() have no return value.
                            B.remove(j)
                            if D[i][encode_city(A)] == 0 or D[i][encode_city(A)] > (W[i][j] + D[j][encode_city(B)]):
                                D[i][encode_city(A)] = W[i][j] + D[j][encode_city(B)]
                                P[i][encode_city(A)] = j
    for j in range(1, n):
        B = copy.deepcopy(V)
        B.remove(j)
        if D[0][encode_city(V)] == 0 or D[0][encode_city(copy.deepcopy(V))] > (W[0][j] + D[j][encode_city(B)]):
            D[0][encode_city(V)] = W[0][j] + D[j][encode_city(B)]
            P[0][encode_city(V)] = j
    min_length = D[0][encode_city(V)]

    print("the min length is :", min_length)


# Set W as weight of edge.
W = [[0, 14, 4, 10, 20], [14, 0, 7, 8, 7], [4, 5, 0, 7, 16], [11, 7, 9, 0, 2], [18, 7, 17, 4, 0]]
TSP_DP(W)