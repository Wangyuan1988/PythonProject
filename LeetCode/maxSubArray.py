from typing import List 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum= nums[0]
        currentSum=0
        for _,v in enumerate(nums):
           if currentSum >0:
               currentSum += v
           else:
               currentSum = v
           maxSum = max(currentSum, maxSum)

        return maxSum

test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4],))
