class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        zerosAmount = nums.count(0)
        if zerosAmount > 1:
            return [0 for i in range(len(nums))]
        # Todo esse esforço para ser O(n) em complexidade de tempo
        if zerosAmount == 1:
            position = -1
            for index in range(len(nums)):
                if nums[index] == 0:
                    position = index
                    break
            finalList = [0 for i in range(len(nums))]
            totalProduct = 1
            for index in range(len(nums)):
                if index == position:
                    continue
                totalProduct = totalProduct * nums[index]
            finalList[position] = totalProduct
            return finalList
        else:
            totalProduct = 1
            finalLista = []
            for index in range(len(nums)):
                totalProduct = totalProduct * nums[index]
            for index in range(len(nums)):
                finalLista.append(totalProduct // nums[index])
            return finalLista

        