class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opening_brackets=['(','{','[']
        closing_brackets=[')','}',']']
        for b in s:
            if b in opening_brackets:
                stack.append(b)
            elif b in closing_brackets:
                id=closing_brackets.index(b)

                if len(stack)==0 or stack.pop()!=opening_brackets[id]:
                    return False

        return len(stack)==0


        
