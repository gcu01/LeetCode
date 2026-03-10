1class Solution(object):
2    def rotateString(self, s, goal):
3        """
4        :type s: str
5        :type goal: str
6        :rtype: bool
7        """
8        '''
9        idx = s.index(goal[0])
10        print("idx = ", idx)
11        print("s[idx:] = ", s[idx:], "   goal[:len(s)-idx-1] = ", goal[:len(s)-idx])                
12        print("s[:idx] = ", s[:idx], "   goal[len(s)-idx:]", goal[len(s)-idx:])
13        if s[idx:] != goal[:len(s)-idx] or s[:idx] != goal[len(s)-idx:]:
14            return False
15        return True
16        '''
17        for i in range(len(s)):
18            if s[i:] + s[:i] == goal:
19                return True
20        return False
21        