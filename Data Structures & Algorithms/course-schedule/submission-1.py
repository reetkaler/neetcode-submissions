class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # [0, 1], [1, 2, 3]

        # build an adjacency list ?
        # courses as nodes (vertices)
        # prerequisites as directed edges
        # there should be no cycles in the graph
        
        # adjacency list is a dictionary where each key is a node
        # each value is the list of nodes pointing INTO it (prerequisites)
        # to get prereqs of a certain course, go to the values of that key iin the adjacency list
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        # cycle occurs if you hit a node currently in your CURRENT dfs path
        visiting = set()

        def dfs(course):
            if preMap[course] == []:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True