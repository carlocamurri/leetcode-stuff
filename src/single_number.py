class Solution:

    def single_number(self, arr):
        appears_once = 0
        for val in arr:
            appears_once ^= val
        return appears_once
