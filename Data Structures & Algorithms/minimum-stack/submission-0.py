class MinStack:

    def __init__(self):
        self.arr= []
        self.minarr=[]

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.minarr.append(min(val,( self.minarr[-1] if self.minarr else float("inf"))))

    def pop(self) -> None:
        self.arr.pop()
        self.minarr.pop()
        
    def top(self) -> int:
        return self.arr[-1]
        
    def getMin(self) -> int:
        return self.minarr[-1]

        
