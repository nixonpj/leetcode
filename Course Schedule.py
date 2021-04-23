"""
There are a total of numCourses courses you have to take, labeled from
0 to numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you
    have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.prereqs = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            self.prereqs[course].append(prereq)
        print(self.prereqs)

        if not prerequisites:
            return True
        self.taken = {i: "Unvisited" for i in range(numCourses)}
        for course in range(numCourses):

            if self.taken[course] == "Unvisited":
                if not self.can_take_course(course):
                    return False
            self.taken[course] = "Visited"
            print("---")
        return True

    def can_take_course(self, course):
        print(course, self.taken)
        self.taken[course] = "Visiting"
        can_take = True
        for prereq in self.prereqs[course]:
            if self.taken[prereq] == "Unvisited":
                if not self.can_take_course(prereq):
                    return False
                # return can_take and self.can_take_course(prereq)
            elif self.taken[prereq] == "Visiting":
                print("cycle", course, prereq, self.taken)
                return False

        self.taken[course] = "Visited"
        return True



s = Solution()
# print(s.canFinish(numCourses=2, prerequisites=[[1,0], [0,1]]))
# print(s.canFinish(numCourses=5, prerequisites=[[1,4],[2,4],[3,1],[3,2]]))
print(s.canFinish(numCourses=5, prerequisites=[[0,1],[1,2],[0,3],[4,0], [3,1], [4,1], [2,4]]))


