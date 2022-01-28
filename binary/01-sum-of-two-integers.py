from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxProfit(self, prices):
        pass



tests = [
    [
        [7,1,5,3,6,4],5
    ],
    [
        [7,6,4,3,1],0
    ],
    [
        [2,4,1],2
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)