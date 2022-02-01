from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def __init__(self):
        self.num = {0:0}

    def maxProfit(self, nums):
        pass

tests = [
    [
        [1,2,3,1], 4
    ],
    [
        [2,7,9,3,1], 12
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)