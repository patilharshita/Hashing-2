# construct longest palindrome with given chars and return length; use a set datastructure in the implementation #
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        
        count =0 
        Set = set()

        for i in range(len(s)):
            c = s[i]
            if c in Set:
                count = count + 2
                Set.remove(c)
            else:
                Set.add(c)
        if len(Set) > 0:
            count = count + 1
        return count
        