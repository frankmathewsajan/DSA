class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
           
            if nums1[i] > nums2[j]:
                result.append(nums2[j])
                j += 1
            else:
                result.append(nums1[i])
                i += 1  
        result.extend(nums1[i:])
        result.extend(nums2[j:])
        rl = len(result)
        median = 0
        if rl % 2 == 0:
            median = (result[rl//2 - 1] + result[rl//2])/2
        else:
            median = result[rl//2]
        return median

        