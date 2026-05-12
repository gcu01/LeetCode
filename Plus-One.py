1class Solution(object):
2    def plusOne(self, digits):
3        """
4        :type digits: List[int]
5        :rtype: List[int]
6        """
7        #if digits[-1] + 1 < 10:
8        #    digits[-1] += 1
9        #    return digits
10        
11        #s = digits[-1] + 1
12        #digits[-1] = s / 10
13        #reminder = s % 10
14        reminder = 1
15        for i in range(len(digits)-1, -1, -1):
16            s = digits[i] + reminder
17            if s == 10:
18                digits[i] = 0
19                reminder = 1
20            elif s < 10:
21                digits[i] += 1
22                break
23            else:
24                digits[i] = s / 10
25                reminder = s % 10
26        #print("reminder = ", reminder)
27        if reminder and digits[0] == 0:
28            digits.insert(0, 1)
29        return digits