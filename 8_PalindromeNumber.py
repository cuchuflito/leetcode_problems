#  Given an integer x, return true if x is palindrome
# integer.

# An integer is a palindrome when it reads the same backward
# as forward.
# For example, 121 is palindrome while 123 is not.

# Input: x = 121
# Output: true

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121.
# From right to left, it becomes 121-. Therefore it is not
# a palindrome.

def solution1(num):

    if num < 0 or num % 10 == 0:
        return False

    # arr = [int(x) for x in str(num)]
    arr = list(map(int, str(num)))
    for i in range(0, len(arr)//2):
        if arr[i] != arr[-(i+1)]:
            return False
    return True


def solution2(num):
    return str(num) == str(num)[::-1]


num = 131
# num = 32123
num = 655
print(solution1(num))
