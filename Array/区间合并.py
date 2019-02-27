# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 14:15
# @Author  : Yippee Song
# @Software: PyCharm


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def toIntervalList(l):
    if not l:
        return l
    else:
        ans = []
        for i in l:
            ans.append(Interval(i[0],i[1]))
        return ans

def show(intervals):
    ans = []
    for i in intervals:
        ans.append([i.start,i.end])
    print ans

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        change = False
        if not intervals:
            return intervals
        intervals.sort(key=lambda x:x.start)
        ans = []
        merged = intervals[0]
        for i in range(1,len(intervals)):
            current = intervals[i]
            if current.end < merged.start or current.start > merged.end:
                ans.append(merged)
                merged = current
            else:
                merged.start = min(merged.start,current.start)
                merged.end = max(merged.end,current.end)
                change = True
        ans.append(merged)
        if not change:
            return ans
        else:
            return self.merge(ans)


if __name__ == '__main__':
    data = [[2,3],[5,5],[2,2],[3,4],[3,4],[2,8]]
    intervals = toIntervalList(data)
    show(Solution().merge(intervals))