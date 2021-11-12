"""
Codility interview problem: a string is "balanced" if each repeating letter in it has an upper case and 
a lower case. For instance, "TACccat" is balanced because letters "t", "c" and "a" appear in both upper 
and lower cases. The string "Hanna" is not balanced because neither "a" nor "n" has its upper case, even 
though they are repeated. The problem is to write a function which returns the length of letters in a balanced 
substring of a string. If there is no balanced substring, then return -1. For example, the string "taCcat" 
has a balanced substring "Cc" and the length of "Cc" is 2. For the string "taccat", there is no balanced
substring, so the function should return -1.

Example 1: "azABaabza"
The function should return 5 because the blanced substring is "ABaab".

Example 2: "TacoCat"
The function should return -1 because "o" and "a" don't have upper cases.

Example 3: "AcZCbaBz"
The function should return 8.

Example 4: "abcdefghijklmnopqrstuvwxyz"
The function should return -1.
"""


def balanced(S):
    a = list(S)
    b = []
    for i in range(len(a)-1):
        c = a[i:i+2]
        for j in range(i+2, len(a)):
            if a[j].lower() in c or a[j].upper() in c:
                if a[j].islower() and a[j].upper() in c:
                    c.append(a[j])
                elif a[j].isupper() and a[j].lower() in c:
                    c.append(a[j])
            elif j+1 < len(a):
                if a[j+1].islower() and a[j+1].upper() in c:
                    c.append(a[j])
                elif a[j+1].isupper() and a[j+1].lower() in c:
                    c.append(a[j])
                else:
                    break
            else:
                break
        b.append(c)
    d = []
    for item in b:
        if len(item) > 2:
            e = [k.lower() for k in item]
            good = True
            for n in e:
                if e.count(n) == 1:
                    good = False
            if good:
                d.append(e)
            else:
                print('e: ', e)
                for m in range(len(e),2,-1):
                    f = e[:m-1]
                    if e[m-1] not in f:
                        e = f
                good = True
                for n in e:
                    if e.count(n) == 1:
                        good = False
                if good:
                    d.append(e)
        else:
            if item[0].islower() and item[1].isupper() or item[1].islower() and item[0].isupper():
                d.append(item)
    if len(d) > 0:
        result = max([len(l) for l in d])
    else:
        result = -1
    return result 

if __name__ == "__main__":
    strs = "azABaabza"
    strs = "TacoCat"
    strs = "AcZCbaBz"
    strs = "abcdefghijklmnopqrstuvwxyz"
    strs = "aa"
    strs = "aAZz"
    print(balanced(strs))

