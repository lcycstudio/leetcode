"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""



def zigzag(input, numRows):
    import string
    # Find a number or alphabet that can be replaced later.
    # We use "PAYPALISHIRING" for example, with numRows = 4.
    num_list = list("0123456789")
    alph_low = list(string. ascii_lowercase)
    alph_upp = list(string. ascii_uppercase)
    check_list = num_list + alph_low + alph_upp
    for item in input:
        if item in check_list:
            check_list.remove(item)
    for_b = check_list[0]
    
    
    a = 0   # increment check for numRows
    b = 0   # increment check for the last entry
    c = 0   # increment check for the zigzag
    n = ""  # string to append
    r = []  # array to append
    l = len(input)  # length of input
    # For item in input, start the increment a and b and add letter to n.
    # If a == numRows, append n to r, e.g., "PAY". Reset a = 0 and set c = 1.
    # If a == numRows - 2, and c > 0, the zigzag takes place and append n to r.
    # Do this until the last entry. If it is the last entry, append n to r.
    for i in input:
        n = n + i
        a += 1
        b += 1
        if a == numRows:
            r.append(n)
            n = ""
            a = 0
            c += 1
        elif a == numRows - 2 and c > 0:
            r.append(n)
            n = ""
            a = 0
            c = 0
        elif b == l:
            r.append(n)
    
    # The outcome of r now looks like this ['PAYP', 'AL', 'ISHI', 'RI', 'NG']
    # For each item in r, if the length of item == numRows, then append it to q.
    # For the zigzag item, such as 'AL', split the string into an array and 
    # convert each item into this form: '00A0' and '0L00', where '0' is for_b.
    q = []
    for j in r:
        a = []
        if len(j) != numRows and j != r[len(r)-1]:
            a = j.split(",")
        b = [for_b] * numRows
        if len(a) == 0:
            if len(j) != numRows:
                for m in range(len(j)):
                    b[m] = j[m]
                j = "".join(b)
            q.append(j)
        else:
            list_a = list(a[0])
            for k in range(len(list_a)):
                b[len(list_a)-k] = list_a[k]
                q.append("".join(b))
                b = [for_b] * numRows
    
    # The outcome of q looks like this ['PAYP', '00A0', '0L00', 'ISHI', '00R0', '0I00', 'NG00']
    # Now we convert the 4x7 matrix into 7x4 matrix. 
    p = [""] * numRows
    for k in q:
        for index in range(len(k)):
            p[index] = p[index] + k[index]
    
    # The outcome of p looks like this ['P00I00N', 'A0LS0IG', 'YA0HR00', 'P00I000']
    # The final step is to join each item into a string and replace "0" with "".
    result = "".join(p).replace(for_b,"")
    return result


if __name__ == "__main__":
    zigzag('PAYPALISHIRING', 4)
    print(zigzag('PAYPALISHIRING', 4))
