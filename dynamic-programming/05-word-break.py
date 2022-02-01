from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def __init__(self):
        self.num = {0:0}

    def maxProfit(self, s, wordDict):
        dp = [False for i in range(len(s)+1)]
        dp[-1] = True
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if (i+len(word)) <= len(s):
                    if s[i: i+len(word)] == word:
                        dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break
        return dp[0]

tests = [
    [
        "leetcode", ["leet","code"], True
    ],
    [
        "applepenapple", ["apple","pen"], True
    ],
    [
        "catsanddog", ["cat","and","cats","dog","sand","and"], True
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)