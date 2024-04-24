class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    def push(self, val: int) -> None:

        self.stack.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)
        return 
        

    def pop(self) -> None:
        if self.stack==[]:
            return None
        else:
            last_val=self.stack.pop(-1)
            if last_val==self.min_stack[-1]:
                self.min_stack.pop(-1)
            return last_val
        

    def top(self) -> int:
        if self.stack==[]:
            return  None
        else:
            return self.stack[-1]


    def getMin(self) -> int:
        if self.stack==[]:
            return  None
        else:
            return self.min_stack[-1]


