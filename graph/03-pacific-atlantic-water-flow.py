from calendar import c
from cmath import inf
from email.policy import default
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
        
        pacific_ocean = [[0 for j in range(len(heights[0]))] for i in range(len(heights))]
        atlantic_ocean = [[0 for j in range(len(heights[0]))] for i in range(len(heights))]
        
        for i, row in enumerate(pacific_ocean):
            for j, cord in enumerate(row):
                if i == 0 or j == 0:
                    pacific_ocean[i][j] = 1
                    
        for i, row in enumerate(atlantic_ocean):
            for j, cord in enumerate(row):
                if i == len(atlantic_ocean)-1 or j == len(row)-1:
                    atlantic_ocean[i][j] = 1

        for i in range(1,len(pacific_ocean)):
            for j in range(1,len(pacific_ocean[0])):
                left_height = heights[i][j-1]
                left_ocean = pacific_ocean[i][j-1]
                up_height = heights[i-1][j]
                up_ocean = pacific_ocean[i-1][j]
                curr_height = heights[i][j]
                if left_height <= curr_height and left_ocean:
                    pacific_ocean[i][j] = 1
                elif up_height <= curr_height and up_ocean:
                        pacific_ocean[i][j] = 1

        for i in range(len(atlantic_ocean)-2,-1,-1):
            for j in range(len(atlantic_ocean[0])-2,-1,-1):
                right_height = heights[i][j+1]
                right_ocean = atlantic_ocean[i][j+1]
                
                down_height = heights[i+1][j]
                down_ocean = atlantic_ocean[i+1][j]
                
                curr_height = heights[i][j]
                if right_height <= curr_height and right_ocean:
                    atlantic_ocean[i][j] = 1
                elif down_height <= curr_height and down_ocean:
                        atlantic_ocean[i][j] = 1
                        
        both_ocean_list = []
        for i, row in enumerate(atlantic_ocean):
            for j, cord in enumerate(row):
                if pacific_ocean[i][j] == 1 and atlantic_ocean[i][j] == 1:
                    both_ocean_list.append([i,j])          
          
        return both_ocean_list
        

tests = [
    [
        [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    ],
    [
        [[2,1],[1,2]],[[0,0],[0,1],[1,0],[1,1]]
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)