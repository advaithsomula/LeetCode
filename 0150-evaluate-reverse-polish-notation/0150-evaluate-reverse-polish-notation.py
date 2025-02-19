class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val_stack=[]
        for i in tokens:
            if i not in {"+","-","*","/"}:
                val_stack.append(int(i))
            else:
                b=val_stack.pop()
                a=val_stack.pop()

                if i =="+":
                    val_stack.append(a+b)
                elif i =="-":
                    val_stack.append(a-b)
                if i =="*":
                    val_stack.append(a*b)
                if i =="/":
                    val_stack.append(int(a/b))
        return val_stack[0]
            
            

        