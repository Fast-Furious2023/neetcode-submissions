class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            elif stack and char in [')','}',']']:
                output = stack.pop()
                if char == ')' and output != '(':
                    return False
                elif char == '}' and output != '{':
                    return False
                elif char == ']' and output != '[':
                    return False
            else:
                return False
            
        return len(stack) == 0

