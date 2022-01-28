from cmath import inf
from math import prod
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxProduct(self, nums, target):
        def binary_search(arr, low , high, target):
            # if low < high:
            #     mid = int((low + high) / 2)
            #     if arr[mid] == target:
            #         return mid
            #     if arr[mid] < target:
            #         return binary_search(arr, mid +1 , high, target)
            #     if arr[mid] > target:
            #         return binary_search(arr, low,mid -1 , target)
            # else:
            #     return -1
            if low <= high:
                mid = int((low + high) / 2)
                if arr[mid] == target:
                    return mid
                if arr[high] >= target:
                    if arr[low] >= target:
                        return binary_search(arr, mid+1, high, target)
                    if arr[low] <= target:
                        if arr[mid] >= target:
                            return binary_search(arr, low, mid-1, target)
                        if arr[mid] <= target:
                            return binary_search(arr, mid+1, high, target)
                if arr[high] <= target:
                    if arr[low] >= target:
                        return binary_search(arr, mid+1, high, target)
                    if arr[low] <= target:
                        if arr[mid] >= target:
                            return binary_search(arr, low, mid-1, target)
                        if arr[mid] <= target:
                            return binary_search(arr, mid+1, high, target)

            else:
                return -1
        ind = binary_search(nums, 0, len(nums)-1, target)
        return ind if ind != -1 else -1
 
 
        

tests = [
    [
        [0,1,2,4,5,6,7], 6, 5
    ],
    [
        [4,5,6,7,0,1,2], 0, 4
    ],
    [
        [4,5,6,7,0,1,2], 3, -1
    ],
    [
        [1], 0, -1
    ]
]

# [1,2,3] 1 2 3 -> 2 < 3 --> [1,2] 1 < 2 --> 
# [3,1,2] 3 2 1 -> 1 < 2 --> [3,1] 3 > 1 --> 1
# [3,1,2] 3 2 1 -> 1 < 2 --> [3,1] 3 > 1 --> 1
# [2,3,1] 2 3 1 -> 3 > 1 --> [3,1] 3 > 1 --> 1

S = Solution()
S.tester(S.maxProduct, tests)