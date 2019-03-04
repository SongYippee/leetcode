# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 15:13
# @Author  : Yippee Song
# @Software: PyCharm

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        if not emails:
            return 0
        ans = set()
        for email in emails:
            localName,domainName = email.split('@')
            indexPlus = localName.find('+')
            if indexPlus>-1:
                localName = localName[0:indexPlus]
            if localName:
                localName = localName.replace('.','')
            ans.add(localName+"@"+domainName)
        return len(ans)