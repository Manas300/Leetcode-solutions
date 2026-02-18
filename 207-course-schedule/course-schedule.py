from typing import List
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency list: graph[pre] = list of courses that depend on 'pre'
        graph = defaultdict(list)

        # indegree[i] = number of prerequisites course i still needs
        indegree = [0] * numCourses

        # Build the graph and indegree array
        for course, prereq in prerequisites:
            # prereq -> course (you must take prereq before course)
            graph[prereq].append(course)

            # course has one more prerequisite
            indegree[course] += 1

        # Queue of all courses that currently have 0 prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Counter for how many courses we are able to finish
        finished = 0

        # Process courses in BFS manner
        while queue:
            curr = queue.popleft()   # Take a course that has no prereqs
            finished += 1            # Mark this course as completed

            # "Unlock" the next courses that depend on curr
            for next_course in graph[curr]:
                indegree[next_course] -= 1  # One prerequisite is now satisfied

                # If next_course has no more prerequisites, we can take it next
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If we managed to finish all courses, return True
        # Otherwise, some courses were stuck in a cycle
        return finished == numCourses
