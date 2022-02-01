from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def __init__(self):
        self.num = {0:0}

    def maxProfit(self, nums):
        hash_table = {}
        visited = []
        max_sub = 1
        for i in range(len(nums)-1,-1,-1):
            hash_table[i] = 1
            if i == len(nums)-1:
                visited.append(i)
            else:
                for j in visited:
                    if nums[i] < nums[j]:
                        hash_table[i] = max(hash_table[i],1 + hash_table[j])
                    else:
                        hash_table[i] = max(1,hash_table[i])
                visited.append(i)
            max_sub = max(max_sub, hash_table[i])
        return max_sub
        
                    

tests = [
    [
        [10,9,2,5,3,7,101,18],4
    ],
    [
        [0,1,0,3,2,3], 4
    ],
    [
        [7,7,7,7,7,7,7], 1
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)