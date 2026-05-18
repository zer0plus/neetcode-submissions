class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 0: return 0
        ans = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                curr += 1
                ans = max(curr, ans)
            elif nums[i-1] == nums[i]:
                continue
            else: curr = 1
        
        return ans