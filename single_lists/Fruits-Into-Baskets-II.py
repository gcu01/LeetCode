1class Solution(object):
2    def numOfUnplacedFruits(self, fruits, baskets):
3        """
4        :type fruits: List[int]
5        :type baskets: List[int]
6        :rtype: int
7        """
8        left = 0
9        empty = [0]*len(baskets)
10        for i in range(len(fruits)):            
11            if baskets == empty:
12                return (len(fruits)-1-i)
13            for j in range(len(baskets)):
14                if baskets[j]>=fruits[i]:
15                    #print("before baskets=", baskets)
16                    #print("fruits[i]=", fruits[i], "   baskets[j]=", baskets[j])
17                    baskets[j] = 0
18                    fruits[i] = 0
19                    #print("after baskets=", baskets)
20                    #print("----------")
21                    break
22            #if i == (len(fruits)-1)
23        fruits = [x for x in fruits if x != 0]
24        return len(fruits)