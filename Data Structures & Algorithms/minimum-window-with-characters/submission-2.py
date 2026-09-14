from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        haveSet = defaultdict(int)
        needSet = defaultdict(int)
        have = 0
        need = 0
        size = len(s)
        res = []
        for i in t:
            needSet[i] += 1
            if needSet[i] == 1:
                need += 1
        l = 0
        for r in range(size):
            if s[r] in needSet.keys():
                haveSet[s[r]] += 1
                if haveSet[s[r]] == needSet[s[r]]:
                    have += 1
            while need == have:
                if res != []:
                    if (res[1] - res[0]) > (r - l):
                        res[0] = l
                        res[1] = r
                if res == []:
                    res.append(l)
                    res.append(r)
                haveSet[s[l]] -= 1
                if s[l] in needSet and haveSet[s[l]] < needSet[s[l]]:
                    have -= 1
                l += 1
        if res == []:
            return ""
        return s[res[0]:res[1]+1]
                




