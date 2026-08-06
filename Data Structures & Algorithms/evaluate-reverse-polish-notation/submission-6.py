
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store=[]
        operators=[]
        res = 0
        for char in tokens:
            if char not in ['+','-','*','/']:
                store.append(int(char))
            else:
                n2=store.pop()
                n1=store.pop()

                if char == '+':
                    store.append(n1+n2)
                elif char == '-':
                    store.append(n1-n2)
                elif char == '*':
                    store.append(n1*n2)
                elif char == '/':
                    store.append(int(n1/n2))

              
        return store[-1]
