"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""



def two_sum(nums, target):
    if 2 > len(nums) or len(nums) > 1e4:
        return "Array length must satisfy the condition: 2 <= length <= 1e4."
    for each in nums:
        if -1e9 > each or each > 1e9:
            return "Each integer must satisfy the condition: -1e9 <= integer <= 1e4."
    if -1e9 > target or target > 1e9:
        return "Target must satisfy the condition: -1e9 <= target <= 1e9."
    
    for i in range(len(nums) - 1):
        result = []
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                break
            if len(result) != 0:
                    break
        if len(result) != 0:
                break
    return result


if __name__ == "__main__":
    nums = [-11**9]
    target = -11**9
    two_sum(nums, target)
    print(two_sum(nums, target))
