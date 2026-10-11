class Solution:
    def getPermutation(self, n, k):
        nums = list(range(1, n + 1))
        k -= 1
        result = ""

        fact = 1
        for i in range(1, n):
            fact *= i

        while nums:
            index = k // fact
            result += str(nums.pop(index))

            if len(nums) == 0:
                break

            k %= fact
            fact //= len(nums)

        return result