from calendar import c
from cmath import inf
from logger import logger_init
from tester import Tester
class Solution(Tester):
    def __init__(self):
        self.num = {0:0}

    def maxProfit(self, text1, text2):
        if len(text1) > len(text2):
            text_short = text2
            text_long = text1
        else:
            text_short = text1
            text_long = text2
        len_common = self.cmonBro(text_short, text_long)
        len_common = max(len_common, self.cmonBro(text_long, text_short))
        return len_common

    def cmonBro(self, text_short, text_long):
        common_text =""
        pointer_short = 0
        pointer_long = 0
        while pointer_long < len(text_long):
            if text_short[pointer_short] == text_long[pointer_long]:
                common_text += text_short[pointer_short]
                text_short = text_short[pointer_short+1:]
                text_long = text_long[pointer_long+1:]
                pointer_long, pointer_short = 0, 0
                if len(text_short) == 0:
                    return len(common_text)
            else:
                if pointer_short < len(text_short)-1:
                    pointer_short += 1
                else:
                    pointer_short = 0
                    pointer_long += 1    
        return len(common_text)
            


            
                    

tests = [
    [
      "oxcpqrsvwf", "shmtulqrypy", 2
    ],
    [
        "ezupkr", "ubmrapg", 2
    ],
    [
        "abcde","gce",2
    ],
    [
        "abcde","ace", 3
    ],
    [
        "abc", "abc", 3
    ],
    [
        "abc", "def", 0
    ]
]

S = Solution()
S.tester(S.maxProfit, tests)