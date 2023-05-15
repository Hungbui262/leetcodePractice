"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while(i < j):
            if s[i].isalnum() == False:
                i +=1
            elif s[j].isalnum() == False:
                j -= 1
            elif (s[i].lower() == s[j].lower()):
                    i +=1
                    j -=1
            else:
                return False
        return True
