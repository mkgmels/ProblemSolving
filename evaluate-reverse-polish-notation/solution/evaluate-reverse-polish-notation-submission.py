class Solution:
    def evalRPN(self, tokens):
        stack=[]
        operators='+-/*'
        for token in tokens:
            if token not in operators:
                stack.append(token)
            elif token in '+-/*':
                operand2=stack.pop()
                operand1=stack.pop()
                if token=='/':
                    result=str(float(operand1)/float(operand2))
                else:
                    result=str(int(float(operand1)))+token+str(int(float(operand2)))

        
                stack.append(str(eval(result)))
        return int(float(stack[0]))

