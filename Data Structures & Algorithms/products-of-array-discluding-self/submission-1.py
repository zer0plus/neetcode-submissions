class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            to_add = 1
            for j in range(len(nums)):
                if j != i: 
                    to_add = to_add * nums[j]
            ans.append(to_add)
        return ans