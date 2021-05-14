"""
Given an m x n grid of characters board and a string word, return true
if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n_rows = len(board)
        self.n_cols = len(board[0])
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:
                    if self.dfs(i, j, [(i, j)], word[1:], board):
                        return True
        # return False

    def dfs(self, i, j, used, word, board):
        if not word:
            print(i, j, word)
            return True
        neighbours = self.find_valid_neighbours(i, j, used)
        print("neighbours", i, j, neighbours, word, used)
        for neighbour_i, neighbour_j in neighbours:
            if board[neighbour_i][neighbour_j] == word[0]:
                # used.append((neighbour_i, neighbour_j))
                if self.dfs(neighbour_i, neighbour_j, used + [(neighbour_i, neighbour_j)], word[1:], board):
                    return True

    def find_valid_neighbours(self, i, j, used):
        res = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        res = [(i, j) for i, j in res
               if 0 <= i < self.n_rows and 0 <= j < self.n_cols and
               (i, j) not in used]  # and visit[row][col] == "unvisited"
        return res


s = Solution()
print(s.exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"))
