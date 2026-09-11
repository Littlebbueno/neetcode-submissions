class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = "".join(c for c in s if c.isalnum())
        falseFlag = False
        for index in range(len(cleanS)):
            if cleanS[index].lower() == cleanS[-1-index].lower():
                continue
            else:
                falseFlag = True

        return not falseFlag
        