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



def two_numbers(l1, l2):
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
    two_numbers(l1, l2)
    print(two_numbers(l1, l2))
