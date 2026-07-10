class Solution:
    def longestPalindrome(self, s: str) -> str:
        #center expansion from i
        

        def centerExpansion(left,right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return right - left - 1
        
        start, end = 0, 0 #index for the longest palindrome so far

        for i in range(len(s)):
            oddlength = centerExpansion(i,i) #odd palindrome: i as center, eg. aba
            evenlength = centerExpansion(i,i+1) #even palindrome: i as left center, eg. abba
            maxlength = max(oddlength, evenlength)

            if maxlength > (end-start):
                start = i - (maxlength-1)//2
                end = i + maxlength//2

        return s[start:end+1]