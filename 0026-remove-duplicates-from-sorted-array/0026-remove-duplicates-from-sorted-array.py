class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       l = 1
       for r in range(1,len(nums)):
        if nums[r] != nums[r-1]: #check if the number is = to the number before
            nums[l] = nums[r] #if not then place nums[r] to nums[l] place
            l += 1 #move the left pointer
       return l #return the index will give the length of the list after removing the duplicates    

