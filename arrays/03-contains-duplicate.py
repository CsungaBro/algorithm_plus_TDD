from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxProfit(self, arr):
        hash_map = {}
        dup = False
        for i, num in enumerate(arr):
            if num in hash_map:
                dup = True
                break
            else:
                hash_map[num] = i
        return dup



tests = [
    [
        [1,2,3,1],True
    ],
    [
        [1,2,3,4],False
    ],
    [
        [1,1,1,3,3,4,3,2,4,2],True
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)