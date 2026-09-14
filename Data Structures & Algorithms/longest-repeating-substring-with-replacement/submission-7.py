from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = defaultdict(int)
        size = len(s)
        l = 0
        for r in range(size):
            count[s[r]] += 1
            mostF = max(count.values())
            sizeW = r - l + 1
            while k < sizeW - mostF and l < r:
                count[s[l]] -= 1
                l += 1
                mostF = max(count.values())
                sizeW = r - l + 1
            if k >= sizeW - mostF:
                if res < sizeW:
                    res = sizeW

        return res
        

        

        
        

