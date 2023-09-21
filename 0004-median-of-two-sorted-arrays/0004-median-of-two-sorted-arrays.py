class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) % 2 != 0:
            return float(nums1[len(nums1)//2])
        
        else:
            m = nums1[len(nums1)//2] + nums1[(len(nums1)// 2) - 1]
            return float(m / 2)
        return 0