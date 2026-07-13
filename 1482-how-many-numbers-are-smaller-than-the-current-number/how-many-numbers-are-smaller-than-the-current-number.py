from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = {}

        # Store the first index of each number
        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i

        result = []

        # Build the answer
        for num in nums:
            result.append(rank[num])

        return result