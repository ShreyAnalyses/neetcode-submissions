# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 for k in range(len(nums)):
#                     if (i != j) and (i != k) and (j != k):
#                         if nums[i] + nums[j] + nums[k] == 0:
#                             if not sorted([nums[i], nums[j], nums[k]]) in result: result.append(sorted([nums[i], nums[j], nums[k]]))


#         return result

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            L = i+1
            R = len(nums) - 1

            target = -1*nums[i]

            while L < R:
                s = nums[L] + nums[R]
                if (s == target) and (not sorted([nums[i], nums[L], nums[R]]) in result):
                    result.append(sorted([nums[i], nums[L], nums[R]]))

                    L+=1
                    R-=1

                elif s < target:
                    L+=1

                else: R-=1

        return result
        