class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # I will import my answer from the 3Sum and do the 4 sum in a similar way.

        def threeSum(nums, target):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res = []

            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                
                left, right = i+1, len(nums)-1
                while left < right:
                    total_sum=nums[i]+nums[left]+nums[right]
                    if total_sum>target:
                        right-=1
                    elif total_sum <target:
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



        res=[]
        nums.sort()
        for i in range(len(nums)-3):
            temp_res = threeSum(nums[i+1:], target-nums[i])

            if temp_res != []:
                for j in temp_res:
                    j.append(nums[i])
                    j.sort()
                    if not (j in res):
                        res.append(j)
        
        return res