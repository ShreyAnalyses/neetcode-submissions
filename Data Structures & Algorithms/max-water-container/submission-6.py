class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mv = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                width = j-i
                v = width*min(heights[i], heights[j])

                mv = v if mv < v else mv

        return mv

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ma = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            width = R - L
            area = width*min(heights[L], heights[R])
            ma = max(ma, area)

            if heights[L] < heights[R]: L += 1
            else: R -= 1

        return ma