from collections import deque

class Solution:

    def combination_sum_iii(self, k, n):
        solutions = []
        current_solution = []
        permutations = self.generate_different_permutations(k, n)
        return permutations

    def generate_different_permutations_helper(self, k, n, current, array, perms):
        if len(array) == k and sum(array) == n:
            perms.append(list(array))
        for i in range(current, 10):
            # choose
            array.append(i)
            # explore
            self.generate_different_permutations_helper(k, n, i + 1, array, perms)
            # un-choose
            array.pop()

    def generate_different_permutations(self, k, n):
        permutations = []
        self.generate_different_permutations_helper(k, n, 1, [], permutations)
        return permutations
