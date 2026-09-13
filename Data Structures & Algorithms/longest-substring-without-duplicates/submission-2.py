class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        maxValue = 0
        l, r = 0, 0
        chars = set()
        while r < size:
            if s[r] not in chars:
                chars.add(s[r])
                r += 1
                maxValue = max(maxValue, r - l)
            else:
                chars.remove(s[l])
                l += 1
        return maxValue

# "abcabcbb"
l = 0
r = 0
maxValue = 0


            

            

        