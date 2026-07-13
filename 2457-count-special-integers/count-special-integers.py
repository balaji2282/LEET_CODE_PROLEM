from functools import lru_cache

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digits = list(map(int, str(n)))

        @lru_cache(None)
        def dp(pos, mask, tight, started):
            if pos == len(digits):
                return 1 if started else 0

            limit = digits[pos] if tight else 9
            ans = 0

            for d in range(limit + 1):
                new_tight = tight and (d == limit)

                if not started and d == 0:
                    ans += dp(pos + 1, mask, new_tight, False)
                else:
                    if mask & (1 << d):
                        continue
                    ans += dp(pos + 1, mask | (1 << d), new_tight, True)

            return ans

        return dp(0, 0, True, False)