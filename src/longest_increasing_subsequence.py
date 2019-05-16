class Solution:

    def longest_increasing_subsequence(self, seq):
        n = len(seq)
        if n == 0:
            return 0
        memo = [1 for _ in range(n)]
        for i in range(1, n):
            inc = [1] + [memo[j] + 1 for j in range(i) if seq[j] < seq[i]]
            memo[i] = max(inc)
        return max(memo)
