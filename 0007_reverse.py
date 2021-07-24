""""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
-2^31 <= x <= 2^31 - 1
"""


import string
def reverse(x):
    # constraints:
    if x < -2**31 or x > 2**31 - 1:
        return "x must be -2^31 <= x <= 2^31 - 1"
    
    # check for valid integer
    try:
        int(x)
    except Exception:
        return "Invalid integer."
    
    # stringify the integer and get "-" sign
    spec = []
    str_x = str(int(x))
    for char in string.punctuation:
        if char in str_x:
            spec.append(char)
            str_x = str_x.replace(char,"")
    
    # get a list of integers
    int_list = []
    for numb in list(str_x):
        try:
            numb = int(numb)
        except Exception:
            pass
        int_list.append(numb)
    
    # reverse order
    new_list = [0] * len(int_list)
    len_ = len(int_list)
    for index in range(len_):
        new_list[len_-1-index] = int_list[index]
    
    # check for preceeding zeros
    for i in range(len_):
        if i < len_ - 1:
            if new_list[0] == "0":
                pass
            elif new_list[i] == "0" and new_list[i-1] == "0":
                pass
            else:
                spec.append(str(new_list[i]))
        else:
            spec.append(str(new_list[i]))
    
    # return the integer
    str_res = ""
    for item in spec:
        str_res += item
    
    result = int(str_res)
    return result


if __name__ == "__main__":
    x = 0
    print(reverse(x))
