class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])
        
        curr_start=intervals[0][0]
        curr_end= intervals[0][1]
        res=[]
        for i in range (1,len(intervals)):
            #if Overlapping update end
            if curr_end>= intervals[i][0]:
                curr_start = min (curr_start, intervals[i][0])
                curr_end = max(curr_end,intervals[i][1])
            # if not overlapping add and start a new one
            else:
                res.append([curr_start,curr_end])
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]
        #add last active since it wouldnt get added until we find a non overlapping new interval
        res.append([curr_start,curr_end])
        return res
            
            
