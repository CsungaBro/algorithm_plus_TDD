from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    
    def maxProfit(self, nums):
        if len(nums) > 2:
            max_first = self.mini_finder(nums[1:])
            max_last = self.mini_finder(nums[:-1])
            return max(max_first, max_last)
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            return nums[0]
    
    def mini_finder(self,nums):
        dp = [0 for i in range(len(nums)+5)]
        for i in range(len(nums)-1,-1,-1):
            dp[i+1] = max(dp[i+3],dp[i+4],dp[i+1])
            dp[i+1] += nums[i]
        dp[0] = max(dp[2],dp[3])       
        return max(dp[0],dp[1]) 


tests = [
    [
      [1,2,3], 3  
    ],
    [
        [2,3,2], 3  
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