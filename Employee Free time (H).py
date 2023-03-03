def freeTime(schedule):
    ans, intervals = [] , []
    
    for s in schedule:
        intervals.extend(s)
        
    intervals.sort(key= lambda x: x[0])
    
    last = intervals[0][1]
    
    for interval in intervals:
        if interval[0] > last:
            ans.append(last, interval[0])
        last = max(last, interval[1])
        
    return ans