from collections import Counter
class Solution:
    def checkValidString(self, s: str) -> bool:
        #a stack for left p, and a stack for star, pop left p first when encounter a right p
        left_stack = []
        star_stack = []

        for i in range(len(s)):
            curr = s[i]
            if curr == '(':
                left_stack.append(i)
            elif curr == '*':
                star_stack.append(i)
            elif curr == ')':
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
       
        while left_stack and star_stack and left_stack[-1] < star_stack[-1]:
            left_stack.pop()
            star_stack.pop()
        
        if left_stack:
            return False
        else:
            return True



            


        