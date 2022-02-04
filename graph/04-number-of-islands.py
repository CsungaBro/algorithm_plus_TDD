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
    def maxProfit(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        islands = {0:set()}
        visited = set()
        
        def dfs(r, c, island_num):
            if ((r,c) in visited or r < 0 or c < 0 or r > ROWS-1 or c > COLS-1):
                return
            if grid[r][c] == "0":
                visited.add((r,c))
                return    
            visited.add((r,c))
            islands[island_num].add((r,c))
            for i in range(-1,2,2):
                dfs(r+i,c,island_num)
                dfs(r,c+i,island_num)
            
        island_number = 0
        for r in range(ROWS):
            for c in range(COLS):
                if not (r,c) in visited:
                    tmp = len(islands[island_number])
                    dfs(r, c, island_number)
                    if tmp != len(islands[island_number]):
                        island_number += 1
                        islands[island_number] = set()
                    
        return len(islands)-1
        
tests = [
    [
      [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ], 3  
    ],
    [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ], 1
    ],
    [
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ], 3
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)