"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def long_minus(l1, l2):
    # constraints
    len_l1 = len(l1)
    len_l2 = len(l2)
    if len_l1 < 1 or len_l1 > 100 or len_l2 < 1 or len_l2 > 100:
        return "The number of nodes in each linked list is in the range [1, 100]."
    if sum(l1) > 9 * len_l1 or sum(l2) > 9 * len_l2:
        return "0 <= Node.val <= 9"
    if l1[0] == 0 or l2[0] == 0:
        return "The list represents a number that does not have leading zeros."
    
    new_l1 = []
    new_l2 = []
    for i in range(len_l1):
        new_l1.append(l1[len_l1-1-i])
    for i in range(len_l2):
        new_l2.append(l2[len_l2-1-i])
    str_l1 = ""
    str_l2 = ""
    for j in new_l1:
        str_l1 += str(j)
    for k in new_l2:
        str_l2 += str(k)
    
    res_list = list(str(int(str_l1)+int(str_l2)))
    res_len = len(res_list)
    result = []
    for l in range(res_len):
        result.append(int(res_list[res_len-1-l]))
    return result


if __name__ == "__main__":
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    long_minus(l1, l2)
    print(long_minus(l1, l2))
