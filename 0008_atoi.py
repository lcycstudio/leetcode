""""
8. String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


Example 1:
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.


Example 2:
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.


Example 3:
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.


Example 4:
Input: s = "words and 987"
Output: 0
Explanation:
Step 1: "words and 987" (no characters read because there is no leading whitespace)
         ^
Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
         ^
The parsed integer is 0 because no digits were read.
Since 0 is in the range [-231, 231 - 1], the final result is 0.


Example 5:
Input: s = "-91283472332"
Output: -2147483648
Explanation:
Step 1: "-91283472332" (no characters read because there is no leading whitespace)
         ^
Step 2: "-91283472332" ('-' is read, so the result should be negative)
          ^
Step 3: "-91283472332" ("91283472332" is read in)
                     ^
The parsed integer is -91283472332.
Since -91283472332 is less than the lower bound of the range [-231, 231 - 1], the final result is clamped to -231 = -2147483648.


Constraints:
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


import string
def atoi(s):
    # constraints:
    if len(s) > 200:
        return "s must be 0 <= s.length <= 200."
    s_list = list(s)
    valid_char = [' ', '+', '-', '.']
    no_dot_char = [' ', '+', '-']
    num_list = list('0123456789')
    invalid_char = []
    for char in string.punctuation:
        if char in s_list and char in no_dot_char:
            char_index = s_list.index(char)
            if char_index != 0 and s_list[char_index - 1] in num_list:
                return "Invalid integer is found."
        if char in s_list and char not in valid_char:
            invalid_char.append(char)
        if char in s_list and char == ".":
            dot_index = s_list.index(".")
            if dot_index + 1 < len(s_list):
                for i in range(dot_index+1, len(s_list)):
                    if s_list[i] != "0":
                        return "Invalid integer is found."
    if len(invalid_char) > 0:
        return "s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'"
    
    if "." in s_list:
        s_list = s_list[:s_list.index(".")]
    
    alph_low = list(string. ascii_lowercase) + [' ']
    alph_upp = list(string. ascii_uppercase) + [' ']
    get_number = []
    get_letter = []
    for j in range(len(s_list)):
        item = s_list[j]
        if (item in alph_low or item in alph_upp == 0) and len(get_number) == 0:
            return 0
        if item in num_list:
            if item == "0" and len(get_number) == 0:
                pass
            if len(get_letter) > 0:
                pass
            else:
                get_number.append(item)
        if (item in alph_low or item in alph_upp) and len(get_number) > 0:
            get_letter.append(item)
    
    str_to_num = {"0": 0,"1": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9}
    result = 0
    for k in range(len(get_number)):
        item = get_number[k]
        e = len(get_number) - 1 - k
        result += str_to_num[item] * 10**e
    
    if "-" in s_list:
        result = -result
    if result < -2**31:
        return -2**31
    elif result > 2**31:
        return 2**31
    return result


if __name__ == "__main__":
    s = "-91283472332"
    print(atoi(s))
