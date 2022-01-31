from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def __init__(self):
        self.num = {0:0}

    def maxProfit(self, coins, target):
        hash_table = {0:0}
        is_the_target_in = False
        curr_target = 1
        while not is_the_target_in:
            curr_min_coin_needed = inf
            for coin in coins:
                if curr_target - coin >= 0:
                    curr_min_coin_needed = min(curr_min_coin_needed, 1 + hash_table[curr_target-coin])
            hash_table[curr_target] = curr_min_coin_needed
            if curr_target >= target:
                is_the_target_in = True
            curr_target += 1
        return hash_table[target] if hash_table[target] != inf else -1


            




tests = [
    [
        [1,2,5],11,3
    ],
    [
        [2],3,-1
    ],
    [
        [1],0
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)