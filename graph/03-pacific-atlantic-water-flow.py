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
    val : list = field(default_factory=list)
    height: int = field(default_factory=int)
    parents : list = field(default_factory=list)
    childs : list = field(default_factory=list)
        
class Solution(Tester):    
    def maxProfit(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prev_height):
            if ((r, c) in visit or
                r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or
                heights[r][c] < prev_height):
                return
            visit.add((r,c))
            for i in range(-1,2,2):
                dfs(r+i, c, visit, heights[r][c])
                dfs(r, c+i, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])        
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])

        return res
        
tests = [
    [
        [[1,2,3],[8,9,4],[7,6,5]], [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    ],
    [
        [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    ],
    [
        [[2,1],[1,2]],[[0,0],[0,1],[1,0],[1,1]]
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)