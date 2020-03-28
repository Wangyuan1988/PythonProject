from typing import List
class Solution:
    @classmethod
    def removeDuplicates(cls, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0

        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]

        print(nums)
        return i + 1

arr=[0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(arr))
        