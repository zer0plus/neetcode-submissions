class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = []*len(prices)

        for i in range(len(prices)):
            max_curr = 0
            for j in range(i+1, len(prices)):
                curr = prices[j]-prices[i]
                max_curr = max(max_curr, curr)
            ans.append(max_curr)

        return max(ans)