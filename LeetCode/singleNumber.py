from typing import List
class Solution:
    @classmethod
    def singleNumber(cls, nums: List[int]) -> int:
        dict={}
        for i,v in enumerate(nums):
            if dict.get(v) is not None:
                del dict[v]
            else:
                dict[v] = i
    
        return list(dict.values())[0]

    @classmethod
    def singleNumberLeetCode(cls, nums: List[int]) -> int:
        dict={}
        for i in nums:
            try:
                dict.pop(i)
            except:
                dict[i]=1
    
        return dict.popitem()[0]

print(Solution.singleNumberLeetCode([2,2,1,1,3]))


        