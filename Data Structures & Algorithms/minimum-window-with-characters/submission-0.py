class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        window = {}
        t_frequency = {}
        l = 0
        count = 0
        

        for i in range(len(t)):
            t_frequency[t[i]] = t_frequency.get(t[i],0) + 1
        
        goal = len(t_frequency)
        
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            if s[r] in t_frequency and window[s[r]]  == t_frequency[s[r]]:
                count += 1
            while count == goal:
                if not result or (r-l+1)<len(result):
                    result = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in t_frequency and window[s[l]] < t_frequency[s[l]]:
                    count -= 1
                l += 1
        return result
            
