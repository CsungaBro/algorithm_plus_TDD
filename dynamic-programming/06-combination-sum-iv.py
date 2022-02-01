from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def __init__(self):
        self.num = {0:0}

    def maxProfit(self, nums, target):
        dp = [0 for i in range(target)]
        for i in range(len(dp)):
            for num in nums:
                nt = i+1 - num
                if nt == 0:
                    dp[i] += 1
                elif nt > 0:
                    dp[i] += dp[nt-1]
        return dp[target-1]

tests = [
    [
        [1,2], 10, 89
    ],
    [
        [1,2,3], 4, 7
    ],
    [
        [9], 3, 0
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)