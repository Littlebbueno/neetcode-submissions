class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {")":"(","}":"{","]":"["}
        stack = []
        for i in range(len(s)):                        
            if i == 0:
                stack.append(s[i])
                continue
            if s[i] in myMap.keys() and stack:                  
                if myMap[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        if stack == []: return True
        return False
        