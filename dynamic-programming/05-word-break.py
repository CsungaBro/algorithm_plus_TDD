from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def __init__(self):
        self.num = {0:0}

    def maxProfit(self, text1, text2):
        pass
            


            
                    

tests = [
    [
        "leetcode", ["leet","code"], True
    ],
    [
        "applepenapple", ["apple","pen"], True
    ],
    [
        "catsandog", ["cats","dog","sand","and","cat"], False
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)