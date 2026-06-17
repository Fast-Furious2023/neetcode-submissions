class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for char in s:
            if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
                filtered.append(char.lower())
        
        left = 0
        right = len(filtered) - 1

        while left <= right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        return True