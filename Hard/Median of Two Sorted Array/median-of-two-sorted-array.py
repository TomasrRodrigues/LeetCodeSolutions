class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Make sure nums1 is the smaller array 
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # x is the length of the smaller array and y the bigger
        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            # Partition nums1
            partitionX = (low + high) // 2
            # Partition nums2 is determined so that left+right halves are equal
            partitionY = (x + y + 1) // 2 - partitionX

            # Handle edge cases with infinities
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if we found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total length is even
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:  # If total length is odd
                    return max(maxLeftX, maxLeftY)
            
            # Move partitionX left
            elif maxLeftX > minRightY:
                high = partitionX - 1

            # Move partitionX right
            else:
                low = partitionX + 1
