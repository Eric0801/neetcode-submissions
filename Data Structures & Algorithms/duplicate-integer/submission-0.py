class Solution: # sorting
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # while using sort, sort the order of elements first to ensure duplicate values are next to each other  
        for i in range(1, len(nums)):
            if nums[i] ==  nums[i-1]:
                return True
        return False