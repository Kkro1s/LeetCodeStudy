def isPalindrome(x):
    xStr = str(x)
    lens = len(xStr)
    left = 0
    if lens%2 == 0:
        return False
    if x < 0:
        return False
    right  = lens -1
    while left < lens/2-1:
        if xStr[left] != xStr[right]:
            return False
        else:
            left +=1
            right -=1
        return True
    # s = str(x)
    # return s == s[::-1]
print(isPalindrome(-21212))


'''
In Python, the syntax s[::-1] is used to reverse a string s.

The slice notation s[start:end:step] is used to extract a part 
of a sequence (such as a string, list, or tuple). The start and
 end indices are optional, and the step value is also optional 
 and defaults to 1. If you leave out the start and end indices, 
 the slice will include all the elements of the sequence.

For example, to reverse a string s, you can use the slice s[::-1]. 
The step value of -1 tells Python to slice the string in reverse 
order, so the resulting slice will be the reverse of the original 
string.


>>> s = 'abcde'
>>> s[::-1]
'dcba'
>>> s = 'abcdefg'
>>> s[::-1]
'gfedcba'
>>> s = 'Hello, World!'
>>> s[::-1]
'!dlroW ,olleH'


'''