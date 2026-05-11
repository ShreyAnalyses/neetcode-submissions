class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mv = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                width = j-i
                v = width*min(heights[i], heights[j])

                mv = v if mv < v else mv

        return mv
