class Solution:
    def numDecodings(self, s: str) -> int:
        #decode into range 1-26, no leading 0 (only 10, 20)
        #decision at every index: cumulatively count
        #1. independently mapped to a letter
        #2.with the previous digit mapped to a letter

        if s[0] == '0':
            return 0
        
        prev2=1 # ways of decode the empty digit
        prev1=1 # ways of decode the first digit

        for i in range(1,len(s)):
            count = 0
            if s[i] != "0":
                count += prev1
            
            two_digit = int(s[i-1:i+1])
            if 10<= two_digit<=26:
                count += prev2
            
            if count == 0:
                return 0
            
            prev2=prev1
            prev1=count
        return prev1


