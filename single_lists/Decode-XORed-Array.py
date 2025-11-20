class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        # convert n to binary 
        #bin(n)[2:]
        out = [0]*(len(encoded)+1)
        out[0] = first
        for i in range(1,len(out)):
            out[i] = out[i-1] ^ encoded[i-1]
        return out 