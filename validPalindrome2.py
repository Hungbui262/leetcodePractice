"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:
Input: s = "aba"
Output: true
Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, i,j):
            while(i < j):
                if(s[i] != s[j]):
                    return False
                else:
                    i += 1
                    j -= 1
            return True
        i = 0
        j = len(s) - 1
        while(i < j):
            if(s[i] != s[j]):
                return checkPalindrome(s,i+1,j) or checkPalindrome(s, i, j-1)
            else:
                i += 1
                j -= 1
        return True
