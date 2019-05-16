class Solution:
    def is_even(self, num):
        return num % 2 == 0

    def array_by_parity(self, arr):
        even = [num for num in arr if self.is_even(num)]
        odd = [num for num in arr if not self.is_even(num)]
        return even + odd
