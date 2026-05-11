class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ta = False # transaction availble status, can not purchase again (before sellling) if have already purchased

        result = 0

        for b in range(len(prices)):
            buy = prices[b]
            for s in range(b+1, len(prices)):
                sell = prices[s]

                result = (sell - buy) if (sell - buy) >  result else result

        return result
                