class Solution:
    def twoSum(self, nums: List[int], target: int):
        nums= nums[::-1]
        
        for i in nums:
            number= target-nums.pop()
            if nums.index(number):
                return i, nums.index(number)
                
        return nums
        