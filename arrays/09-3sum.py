from cmath import inf
from math import prod
from typing import Container
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def maxProduct(self, nums):
        self.quick_sort(nums, 0, len(nums)-1)
        container = []
        for i,num_1 in enumerate(nums):
            target = -1*num_1
            hash_table = {}
            for j, num_2 in enumerate(nums[i+1:]):
                actual = target-num_2
                hash_table[j] = num_2
                if actual in hash_table.values:
                    container.append([num_1, num_2, actual])
        return container
    def partition(self,arr, low, high):
        i = (low -1) 
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] =arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1] 
        return (i+1)
    def quick_sort(self,arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = self.partition(arr, low, high)

            self.quick_sort(arr, low, pi-1)
            self.quick_sort(arr, pi+1, high)


        

tests = [
    [
        [-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]
    ],
    [
        [], []
    ],
    [
        [0], []
    ]
]

# [1,2,3] 1 2 3 -> 2 < 3 --> [1,2] 1 < 2 --> 
# [3,1,2] 3 2 1 -> 1 < 2 --> [3,1] 3 > 1 --> 1
# [3,1,2] 3 2 1 -> 1 < 2 --> [3,1] 3 > 1 --> 1
# [2,3,1] 2 3 1 -> 3 > 1 --> [3,1] 3 > 1 --> 1

S = Solution()
S.tester(S.maxProduct, tests)