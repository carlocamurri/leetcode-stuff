class Solution:

    def array_nesting(self, arr):
        result = 1
        seen = [False] * len(arr)
        for i, val in enumerate(arr):
            count = 0
            j = i
            while not seen[j]:
                seen[j] = True
                count += 1
                j = arr[j]
            result = max(result, count)
        return result
