import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        mid_pos = (len(nums1) + len(nums2)) // 2
        sorted_array = []
        p1 = 0
        p2 = 0
        while len(sorted_array) <= mid_pos:
            if p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    sorted_array.append(nums1[p1])
                    p1 += 1
                else:
                    sorted_array.append(nums2[p2])
                    p2 += 1
            elif p1 == len(nums1):
                sorted_array.append(nums2[p2])
                p2 += 1
            else:
                sorted_array.append(nums1[p1])
                p1 += 1
        if total_len % 2 == 0:
            return (float(sorted_array[-1]) + float(sorted_array[-2])) / 2
        else:
            return float(sorted_array[-1])
