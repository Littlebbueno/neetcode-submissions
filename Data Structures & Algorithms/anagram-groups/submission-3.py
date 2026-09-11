class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        for i in strs:
            sortedStr = "".join(sorted(i))
            if sortedStr not in myMap.keys():
                myMap[sortedStr] = [i]
            else:
                myMap[sortedStr].append(i)
        finalList = []
        for value in myMap.values():
            finalList.append(value)
        return finalList