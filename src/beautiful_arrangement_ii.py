from collections import deque


class Solution:

    def beautiful_arrangement_ii(self, n, k):
        result = list(range(1, n - k))
        pool = deque(range(n - k, n + 1))
        for i in range(len(pool)):
            if i % 2 == 0:
                result.append(pool.popleft())
            else:
                result.append(pool.pop())
        return result
