1class Solution(object):
2    def defangIPaddr(self, address):
3        """
4        :type address: str
5        :rtype: str
6        """
7        i = 0
8        while i < len(address):
9            if address[i] == ".":
10                address = address[:i] + "[.]" + address[i+1:]
11                i += 2
12            i += 1
13        return address 