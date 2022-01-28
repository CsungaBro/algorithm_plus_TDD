from cmath import inf
from math import prod
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxProduct(self, height):
        max_water = 0
        i, j = 0, len(height)-1
        while i < j:
            max_water = max(max_water, (j-i)*min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_water


 
 
        

tests = [
    [
        [1,8,6,2,5,4,8,3,7],49
    ],
    [
        [1,1],1
    ]
]

# [1,2,3] 1 2 3 -> 2 < 3 --> [1,2] 1 < 2 --> 
# [3,1,2] 3 2 1 -> 1 < 2 --> [3,1] 3 > 1 --> 1
# [3,1,2] 3 2 1 -> 1 < 2 --> [3,1] 3 > 1 --> 1
# [2,3,1] 2 3 1 -> 3 > 1 --> [3,1] 3 > 1 --> 1

S = Solution()
S.tester(S.maxProduct, tests)