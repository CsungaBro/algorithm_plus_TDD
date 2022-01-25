from logger import logger_init
from tester import Tester
class Solution(Tester):
    def twoSum(self, nums, target):
        cont = [-1, -1]
        for count, num in enumerate(nums):
            new_nums = nums[count + 1:]
            new_target = target - num
            other_num = self.binary_search(new_nums, 0, len(new_nums)-1, new_target)
            if other_num == -1:
                continue
            else:
                cont = [count, count + other_num + 1] 
                break
        return cont

    def binary_search(self, nums, low, high, target):
        if high >= low:
            mid = int((high + low) // 2)
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                return self.binary_search(nums, low, mid - 1, target)

            elif nums[mid] < target:
                return self.binary_search(nums, mid + 1, high, target)

        else:
            return -1



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
    ]
]

S = Solution()
S.tester(S.twoSum, tests)