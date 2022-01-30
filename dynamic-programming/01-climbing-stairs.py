from logger import logger_init
from tester import Tester
class Solution(Tester):
    def __init__(self):
        self.hash_table = {
            0:0,
            1:1,
            2:2}
    def maxProfit(self, n):
        if n in self.hash_table:
            return self.hash_table[n]
        else:
            tmp = self.maxProfit(n-2) + self.maxProfit(n-1)
            self.hash_table[n] = tmp
            return tmp



tests = [
    [
        4,5
    ],
    [
        2,2
    ],
    [
        3,3
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)