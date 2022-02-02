from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def __init__(self):
        self.num = {0:0}

    def maxProfit(self, nums):
        dp = [0 for i in range(len(nums)+4)]
        for i in range(len(nums)-1,-1,-1):
            dp[i+1] = max(dp[i+3],dp[i+4],dp[i+1])
            dp[i+1] += nums[i]
        dp[0] = max(dp[2],dp[3])           
        return max(dp[0],dp[1]) 


tests = [
    [
      [1,2], 2  
    ],
    [
        [1,2,3,1], 4
    ],
    [
        [2,7,9,3,1], 12
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)