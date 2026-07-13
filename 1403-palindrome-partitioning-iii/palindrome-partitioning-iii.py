class Solution:
    def palindromePartition(self, s, k):
        n = len(s)

        # cost[i][j] = changes needed to make s[i:j+1] palindrome
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] != s[j]:
                    cost[i][j] = cost[i + 1][j - 1] + 1
                else:
                    cost[i][j] = cost[i + 1][j - 1]

        # memoization
        memo = {}

        def dp(index, parts):
            # Last part
            if parts == 1:
                return cost[index][n - 1]

            key = (index, parts)

            if key in memo:
                return memo[key]

            ans = float("inf")

            # Try every possible partition
            for end in range(index, n - parts + 1):
                current = cost[index][end] + dp(end + 1, parts - 1)
                ans = min(ans, current)

            memo[key] = ans
            return ans

        return dp(0, k)