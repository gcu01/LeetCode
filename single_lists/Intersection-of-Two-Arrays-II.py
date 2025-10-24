class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #optimize 1
        out = []
        nums1.sort()
        nums2.sort()
        i = j =0        
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                out.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i +=1
            else:
                j += 1
        return out

        # my version
    '''
        out = []
        for val1 in nums1:
            for val2 in nums2:
                if val1==val2:
                    out.append(val1)
                    nums2.remove(val2)
                    break
        return out 
    '''