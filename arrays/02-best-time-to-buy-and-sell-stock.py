from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxProfit(self, prices):
        low = 0
        high = 0
        profit = 0
        for i, price in enumerate(prices):
            if i == 0: low = price
            if low > price:
                low = price
                high = price
            else:
                if high < price:
                    high = price
            if profit < high - low:
                profit = high -low


        return profit



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