class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

#improved 
        no_nums1 = m-1
        no_nums2 = n-1
        k = n+m-1

        while no_nums1>=0 and no_nums2>=0:
            if nums1[no_nums1] > nums2[no_nums2]:
                nums1[k] = nums1[no_nums1]
                no_nums1 -= 1
            else:
                nums1[k] = nums2[no_nums2]
                no_nums2 -= 1
            k -= 1

        while no_nums2>=0 and k >=0:
            nums1[k] = nums2[no_nums2]
            no_nums2 -= 1
            k -= 1

# my version
'''        
        if m == 0:
            m=n
            nums1=nums2            
            print("nums1=",nums1,"m=",m)
            return nums1
        
        flag = False
        for j, value_nums2 in enumerate(nums2):
            for i, value_nums1 in enumerate(nums1):
                flag = False
                print(value_nums2)
                print(value_nums1)
                if value_nums2 <= value_nums1:
                    nums1.insert(i,value_nums2)
                    print(nums1)
                    nums1.pop()
                    print(nums1)
                    flag = True
                    break
            if flag == 0:                
                nums1.insert(j+n,value_nums2)
                nums1.pop()
        return nums1
'''