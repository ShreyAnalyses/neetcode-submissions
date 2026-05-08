from math import prod
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prefix = [prod(nums[:idx]) for idx in range(len(nums)) ]
#         suffix = [prod(nums[idx+1:]) for idx in range(len(nums)) ]
#         return [prefix[idx]*suffix[idx] for idx in range(len(nums))]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [prod(nums[:idx]) for idx in range(len(nums)) ]
        suffix = [prod(nums[idx+1:]) for idx in range(len(nums)) ]
        return [prefix[idx]*suffix[idx] for idx in range(len(nums))]