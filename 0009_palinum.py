""""
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false

Constraints:
-2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


import string
def palinum(integer):
    # constraints:
    if integer < -2**31 or integer > 2**31 - 1:
        return "Integer must be -2^31 <= x <= 2^31 - 1."

    a = list(str(integer))
    for char in string.punctuation:
        if char in a:
            return False

    len_list = len(a)
    if len_list == 1:
        return False
    if len_list == 2:
        if a[0] == a[1]:
            return True
        else:
            return False
    if a[len_list - 1] != a[0]:
        return False
    
    len_half = int(len_list/2)
    b = a[:len_half]
    c = a[len_half:] if len_list % 2 == 0 else a[len_half+1:]

    result = True
    for i in range(len(b)):
        if b[i] != c[len(b)-1-i]:
            return False
    
    return result


def palinum_no_convert(integer):
    # constraints:
    if integer < -2**31 or integer > 2**31 - 1:
        return "Integer must be -2^31 <= x <= 2^31 - 1."
    
    # check negative
    if integer < 0:
        return False
    
    check = [0, 9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999]
    digit = 0
    for i in range(1, len(check)):
        if integer == check[i] and i > 1:
            return True
        if integer > check[i-1] and integer <= check[i]:
            digit = i
    
    result = True
    if digit == 1:
        result = False
    if digit == 2 and integer % 11 != 0:
        result = False

    a = [1] * digit
    for j in range(digit):
        k = digit - 1 - j
        a[j] = int(integer/(10**k))
        integer = integer - a[j] * 10**k

    half = int(digit/2)
    b = a[:half]
    c = a[half:] if digit % 2 == 0 else a[half+1:]

    for i in range(len(b)):
        if b[i] != c[len(b)-1-i]:
            result = False
            break
    
    return result


if __name__ == "__main__":
    integer = 134
    print(palinum(integer))
    print(palinum_no_convert(integer))

