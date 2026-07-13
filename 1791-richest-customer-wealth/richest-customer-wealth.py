from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0

        for customer in accounts:
            wealth = sum(customer)
            if wealth > maximum:
                maximum = wealth

        return maximum