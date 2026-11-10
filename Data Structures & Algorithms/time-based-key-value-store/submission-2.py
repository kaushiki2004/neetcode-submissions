class TimeMap:

    def __init__(self):
        self.hashMap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr = self.hashMap.get(key,[])
        curr.append([timestamp,value])
        self.hashMap[key] = curr

    def get(self, key: str, timestamp: int) -> str:
        res = self.hashMap.get(key,None)
        if not res:
            return ""
        else:
            l=0
            r=len(res)-1
            while l<=r:
                mid = (l+r)//2
                if res[mid][0] == timestamp:
                    return res[mid][1]
                elif res[mid][0] < timestamp:
                    l = mid +1
                else:
                    r=mid -1
            if r == -1:
                return ""
            else:
                return res[r][1]

        
