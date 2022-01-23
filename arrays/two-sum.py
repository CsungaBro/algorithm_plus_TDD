from logger import logger_init

class Solution:
    def __init__(self) -> None:
        self.tester()

    def twoSum(self, nums, target):
        return [4,5]

    def tester(self):
        tests = [
            [
                [1,2,5,6,8,10,11,15,19],
                18,
                [4,5]
            ],
            [
                [2,7,11,15],
                9,
                [0,1]
            ]
        ]
        for test in tests:
            if self.twoSum(test[0], test[1]) == test[2]:
                logger.info("Passed")
            else:
                logger.error("Failed: {} insted of: {}".format(self.twoSum(test[0], test[1]), test[2]))


logger = logger_init()
S = Solution()