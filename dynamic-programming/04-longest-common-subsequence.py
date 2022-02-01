from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def __init__(self):
        self.num = {0:0}

    def maxProfit(self, text1, text2):
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        print(dp)
        return dp[0][0]
            


            
                    

tests = [
    [
      "oxcpqrsvwf", "shmtulqrypy", 2
    ],
    [
        "ezupkr", "ubmrapg", 2
    ],
    [
        "abcde","gce",2
    ],
    [
        "abcde","ace", 3
    ],
    [
        "abc", "abc", 3
    ],
    [
        "abc", "def", 0
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)