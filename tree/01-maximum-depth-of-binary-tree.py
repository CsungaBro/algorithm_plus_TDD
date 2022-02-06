from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(Tester):    
    def maxProfit(root):
        hash_map = {}
        for counter, node in enumerate(root):
            if counter + 2 <= len(root)-1:
                hash_map[root] = TreeNode(node, root[counter+1], root[counter+2])

tests = [
    [
        [3,9,20,None,None,15,7],3
    ],
    [
        [1,None,2],2
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)