class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Amount of water = area as we don't control depth.
        # I will create two indexes: one to the beginning and one to end of the list
        # I will always move the one acting as a bottle neck.

        start, end = 0, len(height)-1
        max_volume=0 # We can initialize it to 0 as no volume will be negative

        while start<end:
            volume = min(height[start], height[end])* (end-start)
            if volume>max_volume:
                max_volume=volume
            if height[start]>height[end]: end-=1
            else: start+=1
        
        return max_volume

        