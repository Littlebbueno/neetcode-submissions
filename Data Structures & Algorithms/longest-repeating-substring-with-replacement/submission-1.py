from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = defaultdict(int)
        size = len(s)
        total = 0
        l, r = 0, 0
        while r < size:
            myMap[s[r]] += 1
            mostF = max(myMap.values())
            while (r - l + 1) - mostF > k:
                myMap[s[l]] -= 1
                l += 1
            total = max(total, r - l + 1)
            r += 1
        return total

"XYYX"
k = 2



            

        