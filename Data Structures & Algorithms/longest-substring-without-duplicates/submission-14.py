class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            charSet = set()
            charSet.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in charSet:
                    charSet.add(s[j])
                else:
                    break
            print(charSet)
            ans = max(ans, len(charSet))
        return ans