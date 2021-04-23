# Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
# the median of the two sorted arrays.

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Input: nums1 = [2], nums2 = []
# Output: 2.00000

def solution1(list1,list2):
    list3 = list1 + list2
    list3.sort()
    length = len(list3)
    half = length // 2
    # half = len(list3)/2
    if (length % 2 == 0):
        median = (list3[half] + list3[half-1] )/2
    else:
        median = list3[half]
    return median

# nums1 = [1,2]
# nums2 = [3,4]

# nums1 = [0,0]
# nums2 = [0,0]

nums1 = [2]
nums2 = []
print(solution1(nums1,nums2))

