class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                total_sum=nums[i]+nums[left]+nums[right]
                if total_sum>0:
                    right-=1
                elif total_sum <0:
                    left+=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
        
        return res