class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack =[]
        for token in tokens:
            if token in "+-/*":
                val2 = myStack.pop()
                val1 = myStack.pop()
                if token =="+":
                    myStack.append(int(val1) + int(val2))
                elif token=="-":
                    myStack.append(int(val1) - int(val2))
                elif token == "/":
                    myStack.append(int (int(val1) / int(val2)))
                else:
                    myStack.append(int(val1) * int(val2))
            else:
                myStack.append(token)
        return int(myStack[-1])

