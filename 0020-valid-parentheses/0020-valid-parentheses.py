class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={'(':')', '{':'}', '[':']'}
        for i in s:
            if i in brackets:
                stack.append(i)
            elif len(stack)==0 or i!= brackets[stack.pop()]:
                return False

        if len(stack)==0:
            return True
        else: 
            return False

        