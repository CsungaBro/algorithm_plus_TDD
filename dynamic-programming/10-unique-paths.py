from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    
    def maxProfit(self, m, n):
        if m == 1 or n == 1:
            return 1
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        # for i in range(m-2,-1,-1):
        #     dp[i][n-1] = 1
        # for i in range(n-2,-1,-1):
        #     dp[m-1][i] = 1
        # for j in range(n-2,-1,-1):
        #     for i in range(m-2,-1,-1):
        for j in range(n-1,-1,-1):
            for i in range(m-1,-1,-1):                
                if i == m-1 and j != n-1:
                    dp[i][j] = 1    
                elif j == n-1 and i != m-1:
                    dp[i][j] = 1                    
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
                self.dp_printer(dp)
        return dp[0][0]
        
    def dp_printer(self,dp):
        for row in dp[0:-1]:
            print(row[0:-1])
        print("\n")
tests = [
    [
        1, 1, 1
    ],
    [
        3, 2, 3  
    ],
    [
        3, 3, 28
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)