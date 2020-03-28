from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.numArray = nums

    def sumRange(self, i: int, j: int) -> int:
        # if i==j :
        #     return self.numArray[i]
        # else:
        #     return self.sumRange(i+1,j)+self.numArray[i]
        sum = 0
        for k in range(i,j+1):
            sum += self.numArray[k]
        return sum


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,5))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# [-2, 0, 3, -5, 2, -1]