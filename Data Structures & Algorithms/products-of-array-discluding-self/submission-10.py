from math import prod
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prefix = [prod(nums[:idx]) for idx in range(len(nums)) ]
#         suffix = [prod(nums[idx+1:]) for idx in range(len(nums)) ]
#         return [prefix[idx]*suffix[idx] for idx in range(len(nums))]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1 : return [0 for _ in range(len(nums))]
        if nums.count(0) == 1 : return [prod(nums[:idx])*prod(nums[idx+1:]) if nums[idx]==0 else 0 for idx in range(len(nums))]
        return [  prod(nums[:idx])*prod(nums[idx+1:]) for idx in range(len(nums)) ]