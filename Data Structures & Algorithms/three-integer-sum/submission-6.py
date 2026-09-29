class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        mySet = set() 
        ### Debug Area                            
        #     i     j   k
        #[-4,-1,-1, 0,1,2]

        ###
        i, j, k = 0, 1, (len(nums) - 1)    

        while i < len(nums):
            var1 = nums[i]
            while j < k:
                var2 = nums[j]
                var3 = nums[k]
                summ = (var1 + var2 + var3)
                if summ == 0:
                    tupla = (var1, var2, var3)
                    if tupla not in mySet:
                        mySet.add(tupla)
                        res.append([var1, var2, var3])
                    j += 1
                else:
                    if summ < 0:
                        j += 1
                    else:
                        k -= 1
            i += 1
            j = i + 1
            k = len(nums) - 1
        return res

