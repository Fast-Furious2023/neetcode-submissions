class Solution:
    def countSubstrings(self, s: str) -> int:
        #expand from center for i
        # counter
        
        def centerExpand(left,right):#return the number of palindromes
            counter = 0
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left -= 1
                right += 1
                counter += 1
            return counter

        total = 0
        for i in range(len(s)):
            #odd palindrome
            total += centerExpand(i,i)
            #even palindrome
            total += centerExpand(i,i+1)
        return total