from calendar import c
from cmath import inf
from email.policy import default
from re import L
from logger import logger_init
from tester import Tester
from dataclasses import dataclass, field
import matplotlib.pyplot as plt
import numpy as np

@dataclass
class Node:
    val: int = field(default_factory=int)
        
class Solution(Tester):    
    def maxProfit(self, nums):
        nodes = {}
        visited = set()
        longest = 0
        curr = set()
        
        for num in nums:
            nodes[num] = Node(num)

        def dfs(node):
            if node.val in visited:
                return
            visited.add(node.val)
            if node.val-1 in nums:
                dfs(nodes[node.val-1])
            if node.val+1 in nums:
                dfs(nodes[node.val+1])
            
        for num in nums:
            curr.clear()
            visited.clear()
            dfs(nodes[num])
            longest = max (len(visited), longest)
        
        return longest
    
tests = [
    [
        [100,4,200,1,3,2], 4
    ],
    [
        [0,3,7,2,5,8,4,6,0,1], 9
    ]

]

S = Solution()
S.tester(S.maxProfit, tests)