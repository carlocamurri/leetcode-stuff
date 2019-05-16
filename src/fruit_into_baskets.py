class Solution:

    def fruit_into_baskets(self, trees):
        n = len(trees)
        memo = [[1, [trees[i]]] for i in range(n)]
        for i in range(1, n):
            previous_type = memo[i - 1][1]
            if trees[i] in previous_type:
                memo[i][0] = memo[i - 1][0] + 1
            else:
                new_type = [trees[i], trees[i - 1]]
                count = 1
                for tree in reversed(trees[:i]):
                    if tree in new_type:
                        count += 1
                    else:
                        break
                memo[i][0] = count
                memo[i][1] = new_type
        return max(memo, key=lambda x: x[0])[0]

