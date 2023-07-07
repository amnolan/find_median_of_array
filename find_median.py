# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class FindMedian:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge arrays and sort
        nums3 = nums1 + nums2
        nums3.sort()

        # if the array is even just find the TWO midpoints, add them together and divide by 2 median is found
        if len(nums3) % 2 == 0:
            # even
            # if even you need to calculate using 
            # for instance size 20 would be
            # 0 -> 9, 10 -> 19
            # add indexes of 9 and 10 and divide by 2
            length_divided = len(nums3) // 2
            length_divided_a = length_divided - 1
            length_divided_b = length_divided
            median = (nums3[length_divided_a] + nums3[length_divided_b]) / 2 
            return median
        else:
            # it's odd, simple case return the midpoint
            # divide the array in 2 and ceiling the number
            # then add one to account for 
            # zero-based indexing
            length_divided = math.ceil(len(nums3) / 2)-1            
            return nums3[length_divided]
