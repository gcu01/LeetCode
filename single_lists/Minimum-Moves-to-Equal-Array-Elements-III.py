1class Solution(object):
2    def minMoves(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        maxim = max(nums)
8        return len(nums)*maxim - sum(nums)
9        '''
10        moves = 0
11        for val in nums:
12            moves += maxim-val
13        return moves
14        '''