class Solution:

    def subsets(self, arr):
        subsets = []
        for i in range(2 ** len(arr)):
            subset = []
            for j, val in enumerate(arr):
                if 1 << len(arr) - j - 1 & i:
                    subset.append(val)
            subsets.append(subset)
        return subsets
