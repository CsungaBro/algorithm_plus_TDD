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
        def plotter():
            plt.figure()
            to_plot = np.array(heights)
            print(to_plot)
            plt.imshow(to_plot)
            plt.colorbar()
            plt.show()  
        # plotter()
        
        nodes = {}
        
        heights_with_ocean = [[0 for j in range(len(heights[0])+2)] for i in range(len(heights)+2)]
        for i in range(len(heights)+1):
            for j in range(len(heights[0])+1):
                if i > 0 and i < len(heights)+1:
                    if j > 0 and j < len(heights[0])+1:
                        heights_with_ocean[i][j] = heights[i-1][j-1]
                        nodes[str(i)+str(j)] = Node([i,j],heights[i-1][j-1])
                    else:
                        nodes[str(i)+str(j)] = Node([i,j],0)
                else:
                    nodes[str(i)+str(j)] = Node([i,j],0)
        print(np.array(heights_with_ocean))
        
        def neighbour_cheker(x,y):
            x = int(x)
            y = int(y)
            for i in range(-1,2,2):
                for j in range(-1,2,2):
                    if nodes[str(x+i)+str(y+j)].height <= nodes[str(x)+str(y)].height:
                        nodes[str(x)+str(y)].childs.append(nodes[str(x+i)+str(y+j)])
                    else:
                        nodes[str(x)+str(y)].parents.append(nodes[str(x+i)+str(y+j)])
                        
        for node in nodes:
            if not "0" in node:
                neighbour_cheker(node[0], node[1])
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