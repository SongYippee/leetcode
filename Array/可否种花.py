# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 17:09
# @Author  : Yippee Song
# @Software: PyCharm

'''
605 Can Place Flowers,
相邻两个1是不允许的，中间必须隔开至少一个0

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i=0
        cnt=0
        while i<len(flowerbed):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and ( i==len(flowerbed)-1 or flowerbed[i+1]==0 ):
                cnt+=1
                flowerbed[i]=1
            i+=1
        return cnt>=n