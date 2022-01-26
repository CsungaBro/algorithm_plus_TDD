from cmath import inf
from math import prod
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxProduct(self, nums):
        max_prod = max(nums)
        curr_min, curr_max = 1, 1 
        for num in nums:
            tmp = curr_max * num
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(tmp, num * curr_min, num)
            max_prod = max(max_prod, curr_max)
        return max_prod


tests = [
    [
        [2,3,-2,4],6
    ],
    [
        [-2,0,-1],0
    ]
]
# [1,-1] -> [1],[-1] -> 
# [1,-1,2]- [1],[-1],[2]
# [2,-1,2]- [2],[-1],[2]- [1], [2]
# [-2,1,-3,4,-1,2,1,-5,4]-->[-2,1,-3,4][-1][2,1,-5,4]
# [-2,1,-3,4][-1][2,1,-5,4] --> [-2,1][-3,4][-1][2,1][-5,4] -->[-1][1][-1][3][-1]
# [-3,4,-1,2,1]

S = Solution()
S.tester(S.maxProduct, tests)