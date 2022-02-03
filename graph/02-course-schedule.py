from calendar import c
from cmath import inf
from email.policy import default
from logger import logger_init
from tester import Tester
from dataclasses import dataclass, field


class OldNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []        

@dataclass
class Node:
    val : int
    childs : list = field(default_factory=list)
        
class Solution(Tester):    
    def maxProfit(self, numCourses, prerequisites):
        hash_table = {i: [] for i in range(numCourses)}
        visited = set()
            
        for course, pre in prerequisites:
            hash_table[course].append(pre)

        def dfs(node):
            if node in visited:
               return False
            if hash_table[node] == []:
                return True
            visited.add(node)
            for pre in hash_table[node]:
                if not dfs(pre):
                    return False
            visited.remove(node)
            hash_table[node] = [] 
            return True
            
        for course in hash_table:
            h1 = dfs(course)
            if not h1:
                return False

        return True

tests = [
    [
        4, [[2,0],[1,0],[3,1],[3,2],[1,3]], False
    ],
    [
        2, [[1,0]], True
    ],
    [
        2, [[1,0],[0,1]], False
    ],
    [
        3, [[1,0],[2,0],[1,2]], True    
    ],
    [
        3, [[1,0],[0,2],[2,1]], False
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)