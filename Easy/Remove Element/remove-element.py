class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i,pointer=0,0

        while i<len(nums):
            if nums[i]!=val:
                nums[pointer]=nums[i]
                pointer+=1
            i+=1
            
        return pointer