"""
1. Two Sum

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
import time
import numpy as np

def twoSum(nums, target):
    t = time.time()
    for i in range(len(nums) - 1):
        result = []
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                print('elapsed: ', time.time() - t)
                return result
    print('elapsed: ', time.time() - t)
    return result

class Solution:
    def __init__(self) -> None:
        self.index = 0
        self.incmt = 1
    
    def twoSumBigO(self, nums, target):
        nums = np.array(nums)
        t = time.time()
        for i in range(len(nums)):
            if i > len(nums) - 1:
                return []
            diff = target - nums[i]
            remain = nums[i+1:]
            half = int(len(remain) / 2)
            try:
                indx = np.where(remain[:half] == diff)[0][0]
            except IndexError:
                pass
            else:
                print('elapsed: ', time.time() - t)
                return [i, i+1+indx]
            try:
                indx = np.where(remain[half:] == diff)[0][0]
            except IndexError:
                pass
            else:
                print('elapsed: ', time.time() - t)
                return [i, i+1+indx+half]
        return []


if __name__ == "__main__":
    nums = [n for n in range(1, 10001, 1)]
    target = 19999
    print(Solution().twoSumBigO(nums, target))
    print(twoSum(nums, target))
