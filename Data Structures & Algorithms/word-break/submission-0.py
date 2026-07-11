class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # for i, find a j so that 0-j is true and j-i is true

        wordSet = set(wordDict)# for O(1) lookup
        dp = [False]*(len(s)+1)

        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i]= True
                    break
        return dp[len(s)]