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
    path = []
    for i in node.path:  # because of index
        path.append(i - 1)
    bound = 0
    for i in range(0, len(path) - 1):
        bound = bound + random.randrange(1, n)
    # if the edge is the last of node
    min_num = -1
    for i in range(0, n):
        number = random.randrange(1, n)
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
                    number = random.randrange(1, n)
                    if min_num == -1:
                        min_num = number
                    elif min_num > number:
                        min_num = number
            bound = bound + min_num
    # 4분위 수를 초과하는 경우는 별로 없다고 생각됨. 또한, 노드의 레벨이 높을 수록, 편차는 높아짐.
    if (max_bound > bound or bound > max_bound + n/4) and node.level > 1:
        if random.randrange(0, n) < node.level:
            bound = max_bound + random.randrange(int(n/4), n)
        else :
            bound = max_bound + random.randrange(0, int(n/4))
    return bound


def get_length(node, n):
    length = 0
    path = []
    #for i in node.path:
    #    path.append(i - 1)
    #for i in range(0, len(path) - 1):
    #length = node.bound + random.randrange(0, int(n/4)) # it is natural to have length near bound.
    # 4분위수를 고려해봄.
    if random.randrange(0, 4) < 1:
        length = node.bound + random.randrange(int(n/4), n)
    else :
        length = node.bound + random.randrange(0, int(n/4))
    return length


def monte_TSP(N):
    N = int(N)
    PQ = []  # initialize PQ to be empty
    v = Node(0, [1])
    v.bound = get_bound(v, N, 0)
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
print("average node:", tot_node/int(fer_n))