# This will find out minimum path.
import heapq
import copy
import random


class Node:
    def __init__(self, level, path, bound=0):
        self.level = level
        self.path = path
        self.bound = bound

    def __lt__(self, other):
        return self.bound < other.bound

    def __eq__(self, other):
        return self.bound == other.bound


def get_bound(node, n, max_bound):
    bound = n*random.randrange(1, n)
    if (max_bound > bound or bound > max_bound + n) and node.level > 1:
            bound = max_bound + random.randrange(0, n)
    return bound


def get_length(node, n):
    length = node.bound + random.randrange(0, n)
    return length


def monte_TSP(N):
    N = int(N)
    PQ = []  # initialize PQ to be empty
    v = Node(0, [1])
    v.bound = get_bound(v, N, 0)
    min_length = -1  # min_length is infinity
    heapq.heappush(PQ, copy.deepcopy(v))
    u = Node(0, [])
    tot_node = 1
    while PQ:  # PQ is not empty
        v = copy.deepcopy(heapq.heappop(PQ))
        tot_node = tot_node + 1
        if v.bound < min_length or min_length == -1:
            u.level = v.level + 1
            for i in range(2, N + 1):
                if i not in v.path:
                    u.path = copy.deepcopy(v.path)
                    u.path.append(i)
                    if u.level == N - 2:
                        for j in range(1, N + 1):
                            if j not in u.path:
                                last = j
                        u.path.append(last)
                        u.path.append(1)
                        if get_length(u, N) < min_length or min_length == -1:
                            min_length = get_length(u, N)
                    else:
                        u.bound = get_bound(u, N, v.bound)
                        if u.bound < min_length or min_length == -1:
                            heapq.heappush(PQ, copy.deepcopy(u))
    return tot_node


print("CAUTION!")
print("if your computer is not a super computer, \"now testing\" is very long time required.\n")
mat_n = input("What size matrix(n x n) you wnat? ")
fer_n = input("How much do you want perform? ")
tot_node = 0
for i in range(int(fer_n)):
    tot_node = tot_node + monte_TSP(int(mat_n))
    print(i, "done")
print("average node:", tot_node/int(fer_n))