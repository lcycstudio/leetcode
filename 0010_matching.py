""""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false


Constraints:
1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


import string
def matching(s, p):
    # constraints:
    if len(s) < 1 or len(s) > 20:
        return "s must be 1 <= s.length <= 20."
    
    if len(p) < 1 or len(p) > 20:
        return "p must be 1 <= p.length <= 20."
    alph_low = list(string. ascii_lowercase)
    alph_low_plus = alph_low + ['.'] + ['*']
    ls = list(s)
    lp = list(p)
    cs = []
    for item in ls:
        if item not in alph_low:
            cs.append(item)
    if len(cs) > 0:
        return "s contains only lowercase English letters."
    cs = []
    for item in lp:
        if item not in alph_low_plus:
            cs.append(item)
    if len(cs) > 0:
        return "s contains only lowercase English letters."

    
    result = False
    if "." not in lp and "*" not in lp:
        if s == p:
            result = True
        # return result
    
    # Input: s = "aa", p = "a*"
    # Input: s = "aab", p = "c*a*b"
    print('lp: ', lp)
    if "." not in lp and "*" in lp:
        lk = []
        if len(lp) == 1:
            return False
        for i in range(len(lp)-1):
            # print('lp[i]: ', lp[i])
            if lp[i] in ls and lp[i+1] == "*":
                len_lk = len(lk)
                for z in range(len(ls)):
                    if ls[z] == lp[i] and z == len_lk:
                        lk.append(ls[z])
            elif lp[i] in ls and lp[i+1] != "*":
                lk.append(lp[i])
            elif lp[i] not in ls:
                lk.append(lp[i])
        lk.append(lp[-1])
        for m in range(1, len(lk)):
            if lk[m] == "*":
                lk[m] = lk[m-1]
        if ls == lk:
            result = True
        
    
    if "." in lp and "*" not in lp:
        lk = []
        for j in range(len(lp)):
            if lp[j] in ls:
                lk.append(lp[j])
        if lk == ls:
            result = True


    if "." in lp and "*" in lp:
        lk = []
        for k in range(len(lp)-1):
            if lp[k] in ls and lp[k+1] == "*":
                len_lk = len(lk)
                for z in range(len(ls)):
                    if ls[z] == lp[k] and z == len_lk:
                        lk.append(ls[z])
            # if lp[k] in ls and lp[k+1] == "*":
            #     for item in ls:
            #         if item == lp[k]:
            #             lk.append(item)
            #         else:
            #             break
            elif lp[k] in ls and lp[k+1] != "*":
                lk.append(lp[k])
            elif lp[k] == "." and lp[k+1] == "*":
                lk.append("*")
            elif lp[k] == "." and lp[k+1] != "*":
                lk.append(".")
            elif lp[k] not in ls:
                lk.append(lp[k])
        lk.append(lp[-1])
        for item in lk:
            if item == "*":
                result = True
            else:
                result = False
        if len(lk) != len(ls):
            result = False
        
        lm = []
        for d in range(len(ls)):
            if d < len(lk) - 1:
                if lk[d] == ls[d] or lk[d] == '*':
                    lm.append(ls[d])
                else:
                    lm.append(lk[d])
            else:
                if lk[-1] == "*":
                    lm.append(ls[d])
                else:
                    lm.append(".")
        if ls == lm:
            result = True
    
    print('ls: ', ls)
    print('lk: ', lk)
    print('lm: ', lm)
    
    return result



if __name__ == "__main__":
    s = "aab"
    s = "mississippi"
    # p = "mis*is*ip*i"
    p = "mis*is*ip*."
    # p = "a*b"
    print(matching(s, p))

