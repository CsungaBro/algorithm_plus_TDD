from cmath import inf
from math import prod
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxProduct(self, nums):
        def binary_search(arr, low , high):
            if low < high:
                mid = int((low + high) / 2)
                if high-low == 1:
                    if arr[high] > arr[low]:
                        return low
                    else:
                        return high
                if arr[mid] < arr[high]:
                    return binary_search(arr, low, mid)
                if arr[mid] > arr[high]:
                    return binary_search(arr, mid, high)
            else:
                return low
        return nums[binary_search(nums, 0, len(nums)-1)]
 
 
        

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

# [1,2,3] 1 2 3 -> 2 < 3 --> [1,2] 1 < 2 --> 
# [3,1,2] 3 2 1 -> 1 < 2 --> [3,1] 3 > 1 --> 1
# [3,1,2] 3 2 1 -> 1 < 2 --> [3,1] 3 > 1 --> 1
# [2,3,1] 2 3 1 -> 3 > 1 --> [3,1] 3 > 1 --> 1

S = Solution()
S.tester(S.maxProduct, tests)