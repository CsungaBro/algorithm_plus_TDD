from logger import logger_init
from tester import Tester
class Solution(Tester):
    def productExceptSelf(self, nums):
        product = 1
        n = len(nums)
        answer = []
        for num in nums:
            answer.append(product)
            product = product * num
        product = 1
        for i in range(n-1,-1,-1):
            answer[i] = answer[i]*product
            product = product * nums[i]
        return answer



tests = [
    [
        [1,2,3,4],[24,12,8,6]
    ],
    [
        [-1,1,0,-3,3],[0,0,9,0,0]
    ]
]

S = Solution()
S.tester(S.productExceptSelf, tests)