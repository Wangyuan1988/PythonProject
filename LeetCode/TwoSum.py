from typing import List


class Solution:
    @classmethod
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i, m in enumerate(nums):
            j = i+1
            while j < size:
                if target == (m+nums[j]):
                    return [i, j]
                else:
                    j += 1

    @classmethod
    def tow_sum_with_dict(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, m in enumerate(nums):
            _dict[m] = i
        for i, m in enumerate(nums):
            j = _dict.get(target-m)
            if j is not None and i != j:
                return [i, j]

    @classmethod
    def tow_sum_with_dict2(cls, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i, m in enumerate(nums):
            if _dict.get(target - m) is not None:
                return [i, _dict.get(target - m)]
            _dict[m] = i
        # print(_dict)


if __name__ == "__main__":
    print(Solution.tow_sum_with_dict2([2,2,3,3,4,4], 6))
 
