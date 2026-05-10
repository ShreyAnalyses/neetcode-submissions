class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # edge case check: empty list
        if not nums: return 0

        nums_s = sorted(nums)
        counter = 1
        maxx = 1
        for i in range(1, len(nums_s)):

            x = nums_s[i] - nums_s[i-1]

            if x == 0:
                continue

            if x == 1:
                counter += 1

            else: 
                maxx = counter if (maxx < counter) else maxx
                counter = 1

        maxx = counter if (maxx < counter) else maxx

        return maxx
