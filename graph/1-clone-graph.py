from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(Tester):    
    def maxProfit(self, node):
        hash_map = {}
        
        def clone(node):
            if node in hash_map:
                return hash_map[node]
            
            copy = Node(node.val)
            hash_map[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        
        return clone(node) if node else None

tests = [
    [
        [[2,4],[1,3],[2,4],[1,3]], [[2,4],[1,3],[2,4],[1,3]]
    ],
    [
        [[]],[[]]
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)