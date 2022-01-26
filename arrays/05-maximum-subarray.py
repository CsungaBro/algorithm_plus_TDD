from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        actual_sum = 0
        for num in nums:
            if actual_sum < 0 :
                actual_sum = 0
            actual_sum = actual_sum + num
            max_sum = max(max_sum, actual_sum)
        return max_sum

tests = [
    [
        [-1],-1
    ],
    [
        [-2,-1],-1
    ],
    [
        [1,2,-3],3
    ],
    [
        [5,4,-1,7,8],23
    ],
    [
        [1],1
    ],
    [
        [-2,1,-3,4,-1,2,1,-5,4],6
    ]
]
# [1,-1] -> [1],[-1] -> 
# [1,-1,2]- [1],[-1],[2]
# [2,-1,2]- [2],[-1],[2]- [1], [2]
# [-2,1,-3,4,-1,2,1,-5,4]-->[-2,1,-3,4][-1][2,1,-5,4]
# [-2,1,-3,4][-1][2,1,-5,4] --> [-2,1][-3,4][-1][2,1][-5,4] -->[-1][1][-1][3][-1]
# [-3,4,-1,2,1]

S = Solution()
S.tester(S.maxSubArray, tests)