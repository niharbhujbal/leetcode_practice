class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_nums1 = m - 1
        index_nums2 = n - 1
        write_index = m + n - 1

        while index_nums2 >= 0:
            if index_nums1 >= 0 and nums1[index_nums1] > nums2[index_nums2]:
                nums1[write_index] = nums1[index_nums1]
                index_nums1 -= 1
            else:
                nums1[write_index] = nums2[index_nums2]
                index_nums2 -= 1

            write_index -= 1
