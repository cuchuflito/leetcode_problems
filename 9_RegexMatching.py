# Given an input string (s) and a pattern (p), implement regular expression matching
# with support for '.' and '*' where:

#     '.' Matches any single character.​​​​
#     '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
#  by repeating 'a' once, it becomes "aa".

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

# Input: s = "mississippi", p = "mis*is*p*."
# Output: false

def solution1(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (solution1(text, pattern[2:]) or
                first_match and solution1(text[1:], pattern))
    else:
        return first_match and solution1(text[1:], pattern[1:])


s = "aab"
p = "c*a*b"

print(solution1(s, p))
