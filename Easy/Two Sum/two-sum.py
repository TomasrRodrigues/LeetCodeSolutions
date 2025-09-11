class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        target_nums = dict({}) # Directory to store numbers:position that we already checked
        for i, num in enumerate(nums):
            complement = target-num     # Complement = number missing to add up to the target. 
                                        # If it has already been checked, get its position.
            if (complement in target_nums):
                return [i, target_nums[complement]]
            target_nums[num]=i
        return []
            

        