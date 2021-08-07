""""
13. Roman to Integer

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
Output: "III"
Input: num = 3

Example 2:
Output: "IV"
Input: num = 4

Example 3:
Output: "IX"
Input: num = 9

Example 4:
Output: "LVIII"
Input: num = 58
Explanation: L = 50, V = 5, III = 3.

Example 5:
Output: "MCMXCIV"
Input: num = 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= num <= 3999
"""


def roman_int(s):
    # constraints:
    if len(s) < 1 or len(s) > 15:
        return "Roman must be 1 <= s.length <= 15."
    allow = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    s_list = list(s)
    for item in s_list:
        if item not in allow:
            return 'Letter %s is not allowed.'%(item)
    
    re_4 = {'IV': 4,'IX': 9,'XL': 40,'XC': 90,'CD': 400,'CM': 900}

    re_a = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    
    a = []
    for key, value in re_4.items():
        if key in s:
            a.append(value)
            s = s.replace(key, "")
    s_list = list(s)
    for item in s_list:
        a.append(re_a[item])
    
    result = sum(a)
    return result


if __name__ == "__main__":
    s = "III"
    s = "IV"
    s = 'VIII'
    s = "IX"
    s = "LVIII"
    s = "MCMXCIV"
    print(roman_int(s))

