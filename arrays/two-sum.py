from logger import logger_init
from tester import Tester
class Solution(Tester):
    def twoSum(self, nums, target):
        hash  = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in hash:
                return [hash[remaining], i]
            else:
                hash[num] = i



tests = [
    [
        [1,2,5,6,8,10,11,15,19],18,[4,5]],
    [
        [2,7,11,15],9,[0,1]
    ],
    [
        [3,2,4],6,[1,2]
    ],
    [
        [3,3],6,[0,1]
    ],
    [
        [0,4,3,0],0,[0,3]        
    ],
    [
        [150,24,79,50,88,345,3],200,[0,3]
    ]
]

S = Solution()
S.tester(S.twoSum, tests)