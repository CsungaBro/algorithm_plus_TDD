from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    
    def maxProfit(self, nums):
        goal = len(nums)-1
        
        for i in range(len(nums)-2,-1,-1):
            if (i + nums[i]) >= goal:
                goal = i
        return goal == 0

        
tests = [
    [
        [2,3,1,1,4], True
    ],
    [
        [3,2,1,0,4], False
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)