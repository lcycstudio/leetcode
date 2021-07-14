""""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two >>>>sorted arrays<<<<.
The overall run time complexity should be O(log (m+n)).


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""


# This function works even for unsorted arrays.
def median_sort(nums1, nums2):
    # constraints:
    if len(nums1) > 1000:
        return "Length of nums1 must be 0 <= m <= 1000."
    if len(nums2) > 1000:
        return "Length of nums2 must be 0 <= m <= 1000."
    for num in nums1:
        if num < -106 or num > 106:
            return "Each number in nums1 must be -106 <= number <= 106."
    for num in nums2:
        if num < -106 or num > 106:
            return "Each number in nums2 must be -106 <= number <= 106."
    
    # sort nums1
    appd1 = []
    sort1 = nums1
    n = len(sort1)
    while n > 0:
        b = sort1[0]
        for j in range(len(sort1)):
            a = sort1[j]
            if a <= b:
                sort1[j] = b
                b = a
            else:
                sort1[j] = a
        appd1.append(b)
        sort1.remove(sort1[0])
        n -= 1
    
    # sort nums2
    appd2 = []
    sort2 = nums2
    n = len(sort2)
    while n > 0:
        b = sort2[0]
        for j in range(len(sort2)):
            a = sort2[j]
            if a <= b:
                sort2[j] = b
                b = a
            else:
                sort2[j] = a
        appd2.append(b)
        sort2.remove(sort2[0])
        n -= 1
    
    # symmetry 
    l1 = len(appd1)
    l2 = len(appd2)
    if l1 <= l2:
        appd3 = [appd2[i] for i in range(l1, l2)]
        appd2 = [appd2[i] for i in range(l1)]
    else:
        appd3 = [appd1[i] for i in range(l2, l1)]
        appd1 = [appd1[i] for i in range(l2)]
        
    
    # merge sort
    i = 0
    j = 0
    a = []
    while (i < len(appd1) and j < len(appd2)):
        if appd1[i] <= appd2[j]:
            a.append(appd1[i])
            i += 1
        elif appd2[j] < appd1[i]:
            a.append(appd2[j])
            j += 1
    for i in range(i,len(appd1)):
        a.append(appd1[i])
    for j in range(j,len(appd2)):
       a.append(appd2[j])
    
    # last part
    appd4 = appd3
    for num in appd3:
        for k in range(len(a)):
            if num <= a[k]:
                a = a[0:k] + [num] + a[k:]
                appd4 = appd4 - [num]
                break
    if len(appd4) > 0:
        a = a + appd4
    
    half = int(len(a)/2)
    if len(a) % 2 == 0:
        result = (a[half-1] + a[half])/2
    else:
        result = a[half]
    
    return result


if __name__ == "__main__":
    # nums1 = [3,2,4,1,5,2,6,4]
    # nums2 = [2,3,5,7,9]
    nums1 = [1,3]
    nums2 = [2]
    print(median_sort(nums1, nums2))
