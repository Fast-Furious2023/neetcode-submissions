class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        string1 = {}
        string2 = {}

        for element in s:
            string1[element] = string1.get(element, 0) + 1
        
        for element in t:
            string2[element] = string2.get(element, 0) + 1
        
        for element in string1:
            if string1[element] != string2.get(element, 0):
                return False
        return True
            
