from cmath import inf
from math import prod
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxProduct(self, nums):
        def binary_search(arr, low, high):
            if low < high:
                mid = int((low + high) / 2)
                if nums[mid] > nums[high]:
                    return binary_search(arr,mid+1,high)
                if nums[mid] < nums[high]:
                    return binary_search(arr, low, mid-1)        
            else:
                return low
        h1 = binary_search(nums, 0, len(nums)-1)
        if h1 == len(nums)-1:
            return nums[0]
        elif h1 == 0:
            return nums[-1]
        else:
            return min(nums[h1-1],nums[h1],nums[h1+1])
        

tests = [
    [
        [3,4,5,1,2],1
    ],
    [
        [4,5,6,7,0,1,2],0
    ],
    [
        [11,13,15,17], 11
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