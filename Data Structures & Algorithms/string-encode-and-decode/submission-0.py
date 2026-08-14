class Solution:

    def encode(self, strs: List[str]) -> str:
        string=''
        delimiter = '#'
        for i in strs:
            num = len(i)
            string+=str(num)+delimiter+i
        return string

    def decode(self, s: str) -> List[str]:
        delimiter = '#'
        arr=[]
        i=0
        
        while i<len(s):
            curr=''
            while s[i]!='#':
                curr+= s[i]
                i+=1
            count = int(curr)

            i+=1

            curr = s[i:i+count]
            arr.append(curr) 
            i+=count

        return arr        
