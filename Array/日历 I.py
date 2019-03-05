# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 14:31
# @Author  : Yippee Song
# @Software: PyCharm

class MyCalendar(object):

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i,j in self.calendar:
            if not (start>=j or end <=i):
                return False
        else:
            self.calendar.append((start,end))
            return True