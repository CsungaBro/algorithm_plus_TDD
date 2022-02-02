from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    
    def maxProfit(self, s):
        dp = [0]*(len(s)+2)
        ds = s+"00"
        last_zero = False
        two_digit_first = [1,2]
        twenty_second = [1,2,3,4,5,6]
        dp[len(s)] = 1
        last_int_s = 1
        for i in range(len(s)-1,-1,-1):
            int_s = int(ds[i])
            if int_s == 0:
                dp[i] = 0
            else:
                if not last_int_s:
                    if int_s in two_digit_first:
                        dp[i] = dp[i+1] + dp[i+2]
                    else:
                        dp[0] = 0
                        break
                else:
                    if int_s == 1:
                        dp[i] = dp[i+1] + dp[i+2]
                    elif int_s == 2 and last_int_s in twenty_second:
                        dp[i] = dp[i+1] + dp[i+2]
                    else:
                        dp[i] = dp[i+1]
                last_zero = False
            last_int_s = int_s
        return dp[0]

tests = [
    [
        "1201234", 3
    ],
    [
      "12", 2  
    ],
    [
        "226", 3  
    ],
    [
        "06", 0
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)