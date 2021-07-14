""""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.


Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


# This function works even for unsorted arrays.
def palindrome(text):
    # constraints:
    
    # return for one or two letters
    s = list(text)
    if len(s) <= 1:
        return text
    elif len(s) == 2:
        return text[0]
    
    # palindrome algorithm
    b = []
    c = []
    d = []
    for j in range(len(s)-1):
        b = [s[j]]
        for i in range(j+1, len(s)):
            len_b = len(b)
            if len_b % 2 == 0:
                if s[i] == b[0]:
                    c.append("".join(b + [s[i]]))
            else:
                if s[i] == b[int(len_b/2)]:
                    c.append("".join(b + [s[i]]))
            b.append(s[i])
    for item in c:
        li = list(item)
        if li[0] == li[-1]:
            d.append(item)
    dd = []
    for item in d:
        li = list(item)
        ok = True
        ha = int(len(li)/2)
        for i in range(ha):
            if li[i] != li[len(li)-1-i]:
                ok = False
                break
        if ok is True:
            dd.append(item)
    d = dd
    # return all if all with the same length
    ok = len(d[0])
    for j in range(1, len(d)):
        if len(d[j]) != ok:
            ok = 0
    if ok != 0:
        return "{0}".format(", ".join(d))

    # find the longest palindrome
    e = [len(item) for item in d]
    f = e[0]
    h = 0
    for k in range(len(e)):
        if e[k] >= f:
            g = f
            f = e[k]
            e[k] = g
            h = k if e[h] == e[k] else h
    h = 0 if e[0] >= f else h
    result = d[h]
    return result


if __name__ == "__main__":
    text = "babad"
    # text = "cbbd"
    # text = "bb"
    # text = "ac"
    text = "civic"
    text = "keayaejkk"
    print(palindrome(text))
