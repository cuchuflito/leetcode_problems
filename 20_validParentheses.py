# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false


def isValid(s: str) -> bool:
    # SET is o(1) instead of tuple or list which is O(N)
    openChars = {'(', '[', '{'}
    #closeChars = (')', ']', '}')
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []

    if(len(s) < 2 or n % 2 != 0):
        return False

    for c in s:
        if c in openChars:
            stack.append(c)
        else:
            # if there is a closeChar before an openChar
            if not stack or not pairs[c] == stack.pop():
                return False

    # if(stack):
    #     return False
    # return True
    return stack == []


s = "()"
s = "()[]{}"
s = "(]"
s = "{{}[][[[]]]}"
s = "{{({})}}"
s = "(("
s = ")["
print(isValid(s))
