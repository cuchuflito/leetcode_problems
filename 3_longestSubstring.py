# Given a string s, find the length of the longest substring without repeating 
# characters.
# Input: s = "abcabcbb"
# Output: 3
# Input: s = "bbbbb"
# Output: 1
# Input: s = "pwwkew"
# Output: 3

def solution1(s):
    count = []
    word = []
    for c in s:
        if c not in word:
            word.append(c)
        else:
            #new word
            if c==word[-1]:
                count.append(len(word))
                word = [c]
            else:
                count.append(len(word))
                index = word.index(c)
                word.append(c)
                word = word[index+1::]
            
            
    count.append(len(word))
    print(word,count)
    return max(count)


def solution2(s):
    dicts = {}
    maxLength = start = 0
    for i,value in enumerate(s):
        if value in dicts:
            sums = dicts[value] + 1
            if sums > start:
                start = sums
        num = i - start + 1
        if num > maxLength:
            maxLength = num
        dicts[value] = i
    return maxLength    
    
def solution3(s):
    #mismo que solution 1 pero mas pythonic
    ans = 0
    sub = ''
    for char in s:
        if char not in sub:
            sub += char
            ans = max(ans,len(sub))
        else:
            cut = sub.index(char)
            sub = sub[cut+1:] + char
    return ans

s="pwwkew"
s="anviaj"
#s="abcabcbbefghaa"
#s="bbb"
#s="dvdf"
s="azbz"
s="abcabcbbf"
out = solution2(s)
print(out)
