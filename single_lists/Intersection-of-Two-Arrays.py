class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #optimization 1
        set1 = set(nums1)
        set2 = set(nums2)
        out = set()
        for val1 in set1:
            for val2 in set2:
                if val1==val2:
                    out.add(val1) 
        return list(out)
        #my version
        '''
        intersection = set()

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    intersection.add(nums2[j])
                    break

        return list(intersection)
        '''