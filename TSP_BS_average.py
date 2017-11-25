# This will find out minimum path. by bound of average.
# Interesting.
import heapq
import copy


class Node:
    def __init__(self, level, path, bound=0):
        self.level = level
        self.path = path
        self.bound = bound

    def __lt__(self, other):
        return self.bound < other.bound

    def __eq__(self, other):
        return self.bound == other.bound


def get_bound(node, w):
    path = []
    for i in node.path:  # because of index
        path.append(i - 1)
    bound = 0
    for i in range(0, len(path) - 1):
        bound = bound + w[path[i]][path[i + 1]]
    # if the edge is the last of node
    min_num = -1
    for i in range(0, len(w)):
        if i not in path:
            if min_num == -1:
                min_num = w[path[-1]][i]
            elif min_num > w[path[-1]][i]:
                min_num = w[path[-1]][i]
    bound = bound + min_num / 2
    # if the edge is not last of node
    for i in range(0, len(w)):
        if i not in path:
            min_num1 = -1
            for j in range(0, len(w)):
                if j not in path[1:] and j != i:
                    if min_num1 == -1:
                        min_num1 = w[i][j]
                    elif min_num1 > w[i][j]:
                        min_num1 = w[i][j]
            min_num2 = -1
            for j in range(0, len(w)):
                if j not in path[1:-1] and j != i:
                    if min_num2 == -1:
                        min_num2 = w[j][i]
                    elif min_num2 > w[j][i]:
                        min_num2 = w[j][i]
            bound = bound + (min_num1 + min_num2) / 2
    return bound


def get_length(node, w):
    length = 0
    path = []
    for i in node.path:
        path.append(i - 1)
    for i in range(0, len(path) - 1):
        length = length + w[path[i]][path[i+1]]
    return length


def TSP_BS_avg(W):
    PQ = []  # initialize PQ to be empty
    v = Node(0, [1])
    v.bound = get_bound(v, W)
    min_length = -1  # min_length is infinity
    heapq.heappush(PQ, copy.deepcopy(v))
    u = Node(0, [])
    opt_tour = []
    tot_node = 0
    while PQ:  # PQ is not empty
        v = copy.deepcopy(heapq.heappop(PQ))
        tot_node = tot_node + 1
        if v.bound < min_length or min_length == -1:
            u.level = v.level + 1
            for i in range(2, len(W) + 1):
                if i not in v.path:
                    u.path = copy.deepcopy(v.path)
                    u.path.append(i)
                    if u.level == len(W) - 2:
                        for j in range(1, len(W) + 1):
                            if j not in u.path:
                                last = j
                        u.path.append(last)
                        u.path.append(1)
                        if get_length(u, W) < min_length or min_length == -1:
                            min_length = get_length(u, W)
                            opt_tour = copy.deepcopy(u.path)
                    else:
                        u.bound = get_bound(u, W)
                        if u.bound < min_length or min_length == -1:
                            heapq.heappush(PQ, copy.deepcopy(u))

    print("the optimal path is : ", opt_tour)
    print("the min_length is : ", min_length)
    print("tot node: ", tot_node)


# Set W as weight of edge.
W = [[0, 14, 4, 10, 20], [14, 0, 7, 8, 7], [4, 5, 0, 7, 16], [11, 7, 9, 0, 2], [18, 7, 17, 4, 0]]
TSP_BS_avg(W)