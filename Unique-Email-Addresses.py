1class Solution(object):
2    def numUniqueEmails(self, emails):
3        """
4        :type emails: List[str]
5        :rtype: int
6        """
7        em = set()
8        for email in emails:
9            idx1 = email.find("@")
10            idx2 = email.find("+")
11            if idx2 != -1:
12                email = email[:idx2] + email[idx1:]
13            idx1 = email.find("@")
14            email = email[:idx1].replace(".", "") + email[idx1:]
15            em.add(email)
16            #print(email)
17        return len(em)