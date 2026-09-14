class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {")": "(", "}": "{", "]": "["}
        pilha = []
        for r in s:
            if r in myDict:
                if pilha and pilha[-1] == myDict[r]:
                    pilha.pop()
                else:
                    return False
            else:
                pilha.append(r)
        return True if not pilha else False

        
