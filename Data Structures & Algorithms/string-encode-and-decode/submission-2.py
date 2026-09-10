class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr = ""
        if strs == []:
            return "empty"
        for index, str in enumerate(strs):
            finalStr += str
            if index < (len(strs)-1):
                finalStr += "specificString"
        return finalStr
            

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        lista = s.split("specificString")
        return lista
