class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array (binary search on the smaller one for efficiency)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = (total + 1) // 2  # size of the left half

        l, r = 0, n1

        while l <= r:
            i = l + (r - l) // 2   # elements taken from nums1
            j = half - i           # elements taken from nums2

            L1 = nums1[i - 1] if i > 0 else float('-inf')
            R1 = nums1[i] if i < n1 else float('inf')
            L2 = nums2[j - 1] if j > 0 else float('-inf')
            R2 = nums2[j] if j < n2 else float('inf')

            if L1 <= R2 and L2 <= R1:
                # valid partition found
                if total % 2 == 1:
                    return max(L1, L2)
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2
            elif L1 > R2:
                # took too many from nums1, shrink i
                r = i - 1
            else:
                # L2 > R1, took too few from nums1, grow i
                l = i + 1

        return -1  # should never reach here if inputs are valid sorted arrays