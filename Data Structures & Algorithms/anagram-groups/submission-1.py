class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for index,value in enumerate(strs):
            # Sorted em string retorna a string como uma lista de caracteres ordenados, por isso devemos usar o join
            sortedValue = ''.join(sorted(value))
            if sortedValue not in anagrams.keys():
                anagrams[sortedValue] = [value]
            else:
                anagrams[sortedValue].append(value)
        return list(anagrams.values())


