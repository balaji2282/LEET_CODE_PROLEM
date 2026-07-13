from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = {}

        # Count the frequency of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        total = 0

        # Add only the unique elements
        for num in count:
            if count[num] == 1:
                total += num

        return total