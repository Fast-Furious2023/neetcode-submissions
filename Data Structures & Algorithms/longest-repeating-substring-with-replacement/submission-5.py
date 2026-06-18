class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #return the length of the longest substring of one repeating character
        count = {}
        l = 0
        longest = 0
        maxq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            maxq = max(maxq, count[s[r]])
            if (r-l+1) - maxq > k:
                
                count[s[l]]-=1
                l += 1
            longest = max(longest, r-l+1)
        return longest