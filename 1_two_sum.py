"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
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
