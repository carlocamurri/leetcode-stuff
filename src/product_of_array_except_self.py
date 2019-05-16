class Solution:

    def product_of_array_except_self(self, arr):
        factor = 1
        base = [1 for _ in range(len(arr))]
        for i in range(len(arr)):
            base[i] = factor
            factor *= arr[i]
        factor = 1
        for i in range(len(arr)-1, -1, -1):
            base[i] *= factor
            factor *= arr[i]
        return base
