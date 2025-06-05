class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens[::-1]:
            if elem not in "+-/*":
                elem = int(elem)
                while stack != [] and not isinstance(stack[-1], str):
                    num = stack.pop()
                    operand = stack.pop()
                    if operand == '+':
                        elem = elem + num  
                    elif operand == '-':
                        elem = elem - num
                    elif operand == '*':
                        elem = elem * num
                    elif operand == '/':
                        elem = int(elem / num)
            stack.append(elem)
        
        return stack.pop()
