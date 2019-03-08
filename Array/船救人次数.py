# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 12:55
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if not people:
            return 0
        people.sort(reverse=True)
        i = 0
        lenN = len(people)
        j = lenN-1
        cnt = 0
        while i<=j:
            cnt+=1
            if people[i]+people[j]<=limit:
                j-=1
            i+=1
        return cnt