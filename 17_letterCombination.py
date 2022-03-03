# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer
# in any order.

# A mapping of digit to letters(just like on the telephone buttons) is
# given below. Note that 1 does not map to any letters.

# upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png

from calendar import c


def solution1(nums):

    hashTable = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    res = []

    # recursive depth first search (not exactly but similar)
    def dfs(index, curStr):
        # recursive base case
        if(len(nums) == len(curStr)):
            res.append(curStr)
            return

        for c in hashTable[nums[index]]:
            dfs(index+1, curStr + c)

    # case: empty nums
    if len(nums) == 0:
        return res

    dfs(0, '')
    return res


print(solution1("23"))
print(solution1("234"))


#             .
#        /    |      \
#     a       b        c
#    /|\     /|\      /|\
#   d e f   d e f     d e f

# recurisve backtracing

def solution2(nums):
    hashTable = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    res = []

    if(len(nums) == 0):
        return res

    res.append('')

    for n in nums:
        tmp = list()
        chars = hashTable[n]
        for r in res:
            for c in chars:
                tmp.append(r + c)
        res = tmp

    return res


print(solution2("23"))
print(solution2("234"))
