class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #calculate number of intervals that are non overlaping
        #sort the intervals in ascending order
        intervals.sort(key=lambda interval:interval[0])
        max_nonoverlap=1
        last_end = intervals[0][1]
        
        for start,end in intervals[1:]:
            if last_end<= start:
                max_nonoverlap+=1
                last_end= end
            else:
                last_end = min(last_end,end)
        return len(intervals) - max_nonoverlap
