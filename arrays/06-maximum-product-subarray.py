from cmath import inf
from math import prod
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxProduct(self, nums):
        product = nums[0]
        min_product = 1 
        max_product = 1
        for num in nums:
            temp = max_product
            max_product = max(max_product * num, min_product * num, num)
            max_product = min(temp * num, min_product * num, num)
            product = max(product, min_product, max_product)
        return product


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