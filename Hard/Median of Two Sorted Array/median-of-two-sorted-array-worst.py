class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        left1_index = 0
        left2_index = 0
        right1_index = len(nums1)-1
        right2_index = len(nums2)-1
        while True:
            if (right1_index-left1_index+1)+(right2_index-left2_index+1)==1:
                if (right1_index-left1_index+1)==1:
                    return nums1[right1_index]
                else:
                    return nums2[right2_index]
            elif (right1_index-left1_index+1)+(right2_index-left2_index+1)==2:
                if (right1_index-left1_index+1==2):
                    return round((nums1[right1_index]+nums1[left1_index])/2.0,5)
                elif (right2_index-left2_index+1==2):
                    return round((nums2[right2_index]+nums2[left2_index])/2.0,5)
                else:
                    return round((nums1[left1_index]+nums2[right2_index])/2.0, 5)
            
            else:
                if (left1_index<=right1_index and left2_index<=right2_index):
                    if (nums1[left1_index]<nums2[left2_index]):
                        left1_index+=1
                    else:
                        left2_index+=1
                    
                    if (nums1[right1_index]<=nums2[right2_index]):
                        right2_index-=1
                    else:
                        right1_index-=1
                elif (left1_index<=right1_index):
                    left1_index+=1
                    right1_index-=1
                else:
                    left2_index+=1
                    right2_index-=1

