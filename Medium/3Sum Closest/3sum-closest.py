class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        nums.sort()

        closest = float("-inf")

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                total_sum=nums[i]+nums[left]+nums[right]
                temp = total_sum
                if abs(target-temp)<abs(target-closest):
                    closest = temp
                if total_sum>target:
                    right-=1
                elif total_sum <target:
                    left+=1
                else:
                    return target
        
        return closest