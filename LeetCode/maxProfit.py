from typing import List
import sys
class Solution:
    @classmethod
    def maxProfit(cls, prices: List[int]) -> int:
        minValue = sys.maxsize
        maxProfit=0
        for _,v in enumerate(prices):
            if v < minValue:
                minValue = v
                # maxProfit += minValue-v  
            else:
                if v-minValue>maxProfit:
                    maxProfit=v-minValue

        return maxProfit

print(Solution.maxProfit([7,1,5,3,6,4]))
