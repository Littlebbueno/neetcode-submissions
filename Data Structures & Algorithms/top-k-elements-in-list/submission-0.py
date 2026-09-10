class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        for value in nums:
            if value not in myMap.keys():
                myMap[value] = 1
            else:
                myMap[value] += 1
        sortedKeys = list(myMap.keys())
        sortedKeys.sort(key=lambda x: myMap[x])
        sortedKeys.reverse()
        return sortedKeys[0:k]

