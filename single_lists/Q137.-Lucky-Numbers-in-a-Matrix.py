class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lucky = []
        for i in range(len(matrix)):
            minim = min(matrix[i])
            j = matrix[i].index(minim)
            lucky_flag = True
            for k in range(len(matrix)):
                if minim < matrix[k][j]:
                    lucky_flag = False
                    break
            if lucky_flag == True:
                lucky.append(minim)
            #print(j)
            #break
        return lucky