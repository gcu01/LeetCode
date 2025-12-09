1class Solution(object):
2    def hardestWorker(self, n, logs):
3        """
4        :type n: int
5        :type logs: List[List[int]]
6        :rtype: int
7        """
8        maxim = logs[0][1]
9        id = logs[0][0]
10        #print("max = ", maxim, "  id=", id)
11        for i in range(1,len(logs)):
12            #print("logs[",i-1,"][1]=", logs[i-1][1],"logs[",i,"][1]=", logs[i][1])
13            if maxim < (logs[i][1]-logs[i-1][1]):
14                maxim = logs[i][1]-logs[i-1][1]                
15                id = logs[i][0]
16                #print("maxim = ", maxim, "  id=", id)
17            elif maxim == (logs[i][1]-logs[i-1][1]):
18                if id > logs[i][0]:
19                    id = logs[i][0]
20        return id
21            