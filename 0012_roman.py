""""
12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Example 3:
Input: num = 9
Output: "IX"

Example 4:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= num <= 3999
"""


def roman(num):
    # constraints:
    if num < 1 or num > 3999:
        return "Number must be 1 <= num <= 3999."
    
    a = [9,99,999,9999]
    b = []
    for i in range(len(a)):
        if num <= a[i]:
            b = [0] * (i+1)
            for j in range(i, 0, -1):
                b[j] = int(num / 10**j) * 10**j
                num = num % 10**j
            b[0] = num
            break
    f = [4,40,400,4000]
    n = [9,90,900,9000]
    rf = ["IV", "XL", "CD"]
    rn = ["IX", "XC", "CM"]
    c = ["I", "X", "C", "M"]
    d = ["V", "L", "D"]
    r = []
    for k in range(len(b)):
        m = 5 * 10**k
        if b[k] == f[k]:
            r.append(rf[k])
        elif b[k] == n[k]:
            r.append(rn[k])
        elif b[k] % m == 0:
            r.append(d[k])
        elif b[k] < m:
            r.append(c[k]*int((b[k] % m) / 10**k))
        elif b[k] > m:
            r.append(d[k] + c[k]* int((b[k] % m) / 10**k))
    
    result = ''
    for g in range(len(r)):
        result+=r[len(r)-1-g]
    return result


if __name__ == "__main__":
    num = 3
    num = 4
    num = 9
    num = 49
    num = 54
    num = 1994
    print(roman(num))

