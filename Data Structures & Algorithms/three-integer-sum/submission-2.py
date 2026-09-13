class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalList = []
        sortedNums = sorted(nums)
        size = len(sortedNums)
        index = 0
        for index in range(size):
            l, r = (index + 1), (size - 1)
            if (index - 1) >= 0:
                if sortedNums[index] == sortedNums[index -1]:
                    continue
            while l < r:
                soma = sortedNums[index] + sortedNums[r] + sortedNums[l]
                if soma == 0:
                    item = [sortedNums[index], sortedNums[r], sortedNums[l]]
                    finalList.append(item)
                    l += 1
                    while sortedNums[l-1] == sortedNums[l] and l < r:
                        l += 1
                elif soma > 0:
                    r -= 1
                elif soma < 0:
                    l += 1
        return finalList
                


        

            



        
        