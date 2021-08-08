""""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

import string
def long_pre(strs):
    # constraints:
    if len(strs) < 1 or len(strs) > 200:
        return "The string list must be 1 <= strs.length <= 200."
    for item in strs:
        if len(strs) > 200:
            return "Each item must be 0 <= strs[i].length <= 200."
        if item != item.lower():
            return "Each item strs[i] consists of only lower-case English letters."
    
    # algorithm
    pre = []
    for i in range(len(strs)-1):
        text1 = list(strs[i])
        for j in range(i+1, len(strs)):
            text2 = list(strs[j])
            if len(text1) <= len(text2):
                for k in range(len(text1)):
                    if text1[k] == text2[k]:
                        pre.append((k, text1[k]))
            else:
                for k in range(len(text2)):
                    if text2[k] == text1[k]:
                        pre.append((k, text1[k]))
    
    a = [("","")] * len(strs)
    for n in range(len(strs)):
        for item in pre:
            if pre.count(item) >= n+1:
                if item[1] not in a[n][1]:
                    t = a[n][1]
                    t = t + item[1]
                    p = a[n][0]
                    p = p + str(item[0])
                    a[n] = (p, t)
                elif item[1] in a[n][1] and str(item[0]) not in a[n][0]:
                    t = a[n][1]
                    t = t + item[1]
                    p = a[n][0]
                    p = p + str(item[0])
                    a[n] = (p, t)
    result = ''
    for m in range(len(a)-1, 1, -1):
        if a[m][1] != "":
            result = a[m][1]
            break
    if result == '':
        result = 'There is no common prefix among the input strings.'
    return result


if __name__ == "__main__":
    strs = ["feleower","feleow","feleight"]
    # strs = ["dog","racecar","car"]
    print(long_pre(strs))

