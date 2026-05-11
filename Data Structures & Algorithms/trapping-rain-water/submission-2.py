class Solution:
    def trap(self, height: List[int]) -> int:
        
        def maxAreaAtAPosition(i, height):

            if (i == 0) or (i == len(height) - 1):
                return 0
            
            L,R = i,i
            hL, hR = 0,0

            while L >= 0:
                hL = height[L] if height[L] > hL else hL
                L -= 1

            while R <= len(height) - 1:
                hR = height[R] if height[R] > hR else hR
                R += 1

            return max(min(hL, hR) - height[i], 0)
        

        trap_amount = 0
        for i in range(len(height)):
            trap_amount += maxAreaAtAPosition(i, height)
        
        return trap_amount