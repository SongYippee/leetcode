# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 14:59
# @Author  : Yippee Song
# @Software: PyCharm
import collections
import bisect

class MyCalendarThree:

    def __init__(self):
        self.history = [float('inf') for _ in range(400)]
        self.counter = collections.Counter()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        if start not in self.counter:
            bisect.insort(self.history, start)
        if end not in self.counter:
            bisect.insort(self.history, end)
        self.counter[start] += 1
        self.counter[end] -= 1

        active = maxDuplicateTimes = 0
        for i in range(len(self.counter)):
            active += self.counter[self.history[i]]
            if active > maxDuplicateTimes:
                maxDuplicateTimes = active
        return maxDuplicateTimes

if __name__ == '__main__':
    calendar = MyCalendarThree()
    print calendar.book(10,20)
    print calendar.book(50,60)
    print calendar.book(10,40)
    print calendar.book(5,15)
    print calendar.book(5,10)
    print calendar.book(25,55)