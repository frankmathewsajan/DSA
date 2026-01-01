class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x, y = len(nums1), len(nums2)
        u, v = 0, x
        while u <= v:
            i = (u + v) // 2
            j = (x + y + 1) // 2 - i
            a = float('-inf') if i == 0 else nums1[i-1]
            b = float('inf') if i == x else nums1[i]
            c = float('-inf') if j == 0 else nums2[j-1]
            d = float('inf') if j == y else nums2[j]

            if a <= d and c <= b:
                
                if (x+y)%2 == 0:
                    return (max(a,c) + min(b,d))/2
                else:
                    return max(a,c)    
            elif a > d:
                v = i - 1
            else: 
                u = i + 1

"""
Median of Two Sorted Arrays
1. Make sure nums1 is the smaller array
2. Perform binary search on nums1 i = (u + v) // 2
3. Calculate the corresponding index j in nums2 j = (x + y + 1) // 2 - i
4. Compare the elements around the partition points and adjust the binary search range accordingly.

A B
C D

A <-> D :: B <-> C
if even:
    median = (max(A,C) + min(B,D))/2
else:
    median = max(A,C)

if A > D:
    v = i - 1
else:
    u = i + 1
"""   