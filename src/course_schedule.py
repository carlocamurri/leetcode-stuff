class Solution:

    def course_schedule(self, numCourses, prerequisites):
        dependencies = [0 for i in range(numCourses)]
        edges = [[] for i in range(numCourses)]

        order = []

        for complete_after, complete_before in prerequisites:
            dependencies[complete_after] += 1
            edges[complete_before].append(complete_after)

        def find_non_dependency():
            print(dependencies)
            for i, deps in enumerate(dependencies):
                if deps == 0:
                    return i

        def incest(node):
            for es in edges[node]:
                dependencies[es] -= 1

        while len(order) < numCourses:
            non_dependency = find_non_dependency()

            if non_dependency is None:
                return False

            order.append(non_dependency)
            dependencies[non_dependency] -= 1

            incest(non_dependency)

        return True

