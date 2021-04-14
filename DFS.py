"""
Practice DFS from scratch

(1,3), (2,4), (0,1), (1,2), (2, 0)


            0
          /   \
        1  -->  2
      /       /
    3  <--  4
"""
from math import inf

def dfs(num_nodes, edges):
    adj_list = create_adj_list(num_nodes, edges)
    colours = {i: "white" for i in range(num_nodes)}
    # parents = {i: None for i in range(num_nodes)}

    for vertex in range(num_nodes):
        if colours[vertex] == "white":
            if not dfs_subroutine(vertex, adj_list, colours):
                return False


def dfs_subroutine(vertex, adj_list, colours):
    colours[vertex] = "grey"
    for adj_vertex in adj_list[vertex]:
        # if colours[adj_vertex] == "grey":
        #     print(vertex, adj_vertex)
        #     return False
        # if colours[adj_vertex] == "black":
        #     print("cross-edge", vertex, adj_vertex)
        if colours[adj_vertex] == "white":
            print("exploring", vertex, adj_vertex)
            dfs_subroutine(adj_vertex, adj_list, colours)
    print(vertex, "is blackened")
    colours[vertex] = "black"


def create_adj_list(num_nodes, edges):
    res = {i:[] for i in range(num_nodes)}
    for edge in edges:
        from_, to_ = edge
        res[from_].append(to_)
    return res


print(dfs(5, [(1,3), (2,4), (0,1), (1,2), (2, 0), (4,3)]))





