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


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mp = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            mp = prices[i] if prices[i] < mp else mp

            profit = prices[i] - mp if prices[i] - mp > profit else profit

        return profit
