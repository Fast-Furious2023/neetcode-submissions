class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for char in s.lower():
            if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
                filtered.append(char)
        
        left = 0
        right = len(filtered) - 1

        while left <= right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        return True