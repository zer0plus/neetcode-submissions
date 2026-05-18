class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # ex = 0, 1, 2, 3, 4, 5, 6, 7 , 8
        # 2, 

        ans = 0
        curr = 0
        for i in range(len(heights)):
            for k in range(1, len(heights)):
                curr = min(heights[i], heights[k]) * (k-i)
                ans = max(curr, ans)

        return ans