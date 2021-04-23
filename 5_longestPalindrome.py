#Given a string s, return the longest palindromic substring in s.

#Input: s = "babad"
# Output: "bab"

# Input: s = "cbbd"
# Output: "bb"

# https://leetcode.com/problems/longest-palindromic-substring/

class Palindrome(object):
    def __init__(self,array):
        self.resultStart = 0
        self.resultLength = 0
        self.s = array

    def searchLongestPalindrome(self):
        s = self.s
        l = len(s)
        if (l<2):
            return s

        for i in range(0,len(s)-1):
            self.expandCenter(i,i)
            self.expandCenter(i,i+1)
        
        return s[self.resultStart:self.resultStart+self.resultLength] 

    def expandCenter(self,begin,end):
        # print(begin,end)
        s = self.s
        # print("start ",begin,end)
        while len(s)>end and begin>=0 and (s[begin]==s[end]):
            begin = begin -1
            end =end + 1
        # print("end ",begin,end)
        if self.resultLength < (end - begin - 1):
            self.resultLength = end - begin - 1
            self.resultStart = begin + 1
            # print("max ",self.resultStart,self.resultLength)

array = "200031"
# array = "1234442"
array = "000"
array = "0012313214"
array = "01"
array="321"
Palin = Palindrome(list(array))

print("Longest Palindrome: ",Palin.searchLongestPalindrome())
print("Palindrome original: ",Palin.s)
print("Palindrome Comienzo ",Palin.resultStart)
print("Palindrome Final",Palin.resultLength)