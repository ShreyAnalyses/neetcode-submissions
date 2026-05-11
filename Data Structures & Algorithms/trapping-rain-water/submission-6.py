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


class Solution:
    def trap(self, height: List[int]) -> int:

        LM, RM = [0]*len(height), [0]*len(height)

        LM[0] = height[0]
        RM[-1] = height[-1]

        for i in range(1, len(height)):
            LM[i] = max(LM[i-1], height[i])

        for i in range(len(height)-2, -1, -1):
            RM[i] = max(RM[i+1], height[i])

        water_trap = 0
        for i in range(len(height)):
            water_trap += (min(LM[i], RM[i]) - height[i])

        return water_trap


























