# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 14:05
# @Author  : Yippee Song
# @Software: PyCharm

class MyCalendarTwo:
    def __init__(self):
        '''
        overlaps存储有两次重叠的区间段
        calendar存储不存在重叠的区间段
        '''
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                '''第三次重叠，不允许插入'''
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                '''
                待插入的 start,end和已存储的 calendar区间有重叠，计算重叠部分的区间段
                '''
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True


if __name__ == '__main__':
    calendar = MyCalendarTwo()
    print calendar.book(10,20)
    print calendar.book(50,60)
    print calendar.book(10,40)
    print calendar.book(5,15)
    print calendar.book(5,10)
    print calendar.book(25,55)