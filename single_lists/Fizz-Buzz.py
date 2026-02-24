1class Solution(object):
2    def fizzBuzz(self, n):
3        """
4        :type n: int
5        :rtype: List[str]
6        """
7        out = [""]*n
8        #print(out)
9        for i in range(n):
10            #print(out)
11            if (i+1)%3 == 0 and (i+1)%5 == 0:
12                out[i] = "FizzBuzz"
13            elif (i+1)%3 == 0:
14                out[i] = "Fizz"
15            elif (i+1)%5 == 0:
16                out[i] = "Buzz"
17            else:
18                out[i] = str(i+1)
19        return out