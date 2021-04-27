"""
You are given an m x n integer matrix heights representing the height
of each unit cell in a continent. The Pacific ocean touches the continent's
left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.

Water can only flow in four directions: up, down, left, and right. Water
flows from a cell to an adjacent one with an equal or lower height.

Return a list of grid coordinates where water can flow to both the
Pacific and Atlantic oceans.

Status: Incomplete
"""
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_rows, n_cols = len(heights), len(heights[0])
        visit = [["unvisited"]*n_cols for _ in range(n_rows)]
        atlantic = [[False] * n_cols for _ in range(n_rows-1)] + [[True]*n_cols]
        pacific = [[True]*n_cols] + [[False] * n_cols for _ in range(n_rows-1)]

        for row in range(n_rows):
            pacific[row][0] = atlantic[row][-1] = True

        print(atlantic)

        def get_valid_neighbours(row, col):
            print(row, col)
            res = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            print(res)
            res = [(row, col) for row, col in res
                    if 0 <= row < n_rows and 0 <= col < n_cols and visit[row][col] == "unvisited"]
            print(res)
            return [(r, c) for r, c in res if heights[r][c] <= heights[row][col]]

        def dfs(row, col):
            visit[row][col] = "visiting"
            if not (atlantic[row][col] and pacific[row][col]):
                neighbours = get_valid_neighbours(row, col, [])

                for neighbour_row, neighbour_col in neighbours:
                    if atlantic[neighbour_row][neighbour_col]:
                        atlantic[row][col] = True
                    if pacific[neighbour_row][neighbour_col]:
                        pacific[row][col] = True
                    dfs(neighbour_row, neighbour_col)
            visit[row][col] = "visited"


        for row in range(n_rows):
            for col in range(n_cols):
                if visit[row][col] == "unvisited":
                    dfs(row, col)

        print(atlantic)





s = Solution()
print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))