class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j and nums[i] + nums[j] == target:
                    return [i,j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapping: return [mapping[diff], i]
            else: mapping[nums[i]] = i
