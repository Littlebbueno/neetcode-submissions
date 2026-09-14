from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = []
        haveSet = defaultdict(int)
        needSet = defaultdict(int)
        need = 0
        have = 0
        size = len(s)
        for value in t:
            needSet[value] += 1
            if needSet[value] == 1:                
                need += 1                          
        l = 0                                      
        for r in range(size):
            haveSet[s[r]] += 1
            if haveSet[s[r]] == needSet[s[r]]:
                have += 1
            while have == need:
                if res == []:
                    res.append(l)
                    res.append(r)
                else:
                    if res[1]-res[0] > r - l:
                        res[0] = l
                        res[1] = r
                haveSet[s[l]] -= 1
                if haveSet[s[l]] < needSet[s[l]]:
                    have -= 1
                l += 1
        if res != []:
            return s[res[0]: res[1]+1]
        else:
            return ""

                

            