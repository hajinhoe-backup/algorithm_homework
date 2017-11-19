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


def get_bound(node, n):
    path = []
    for i in node.path:  # because of index
        path.append(i - 1)
    bound = 0
    for i in range(0, len(path) - 1):
        bound = bound + random.random()
    # if the edge is the last of node
    min_num = -1
    for i in range(0, n):
        number = random.random()
        if i not in path:
            if min_num == -1:
                min_num = number
            elif min_num > number:
                min_num = number
    bound = bound + min_num
    # if the edge is not last of node
    for i in range(0, n):
        if i not in path:
            min_num = -1
            for j in range(0, n):
                if j not in path[1:] and j != i:
                    number = random.random()
                    if min_num == -1:
                        min_num = number
                    elif min_num > number:
                        min_num = number
            bound = bound + min_num
    return bound


def get_length(node, n):
    length = 0
    path = []
    for i in node.path:
        path.append(i - 1)
    for i in range(0, len(path) - 1):
        length = length + random.random()
    return length


# n is the size of n x n matrix.
N = 10

PQ = []  # initialize PQ to be empty
v = Node(0, [1])
v.bound = get_bound(v, N)
min_length = -1  # min_length is infinity
heapq.heappush(PQ, copy.deepcopy(v))
u = Node(0, [])
opt_tour = []
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
                        opt_tour = copy.deepcopy(u.path)
                else:
                    u.bound = get_bound(u, N)
                    if u.bound < min_length or min_length == -1:
                        heapq.heappush(PQ, copy.deepcopy(u))

print("tot_node:", tot_node)