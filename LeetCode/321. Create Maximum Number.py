
from typing import List

class Solution:
    def maxNumber(self,nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ls = [0]
        self.recursion(0,0,nums1,nums2,0,k,ls)
        return ls[0]

    def recursion(self,p1,p2,nums1,nums2,temp_num ,k,ls):
        if k == 0:
            if temp_num > ls[0]:
                ls[0] = temp_num
        
        if p1 < len(nums1):
            # choose curr el from nums1
            self.recursion(p1+1,p2,nums1,nums2,temp_num*10+nums1[p1],k-1,ls)
            # leave curr el from nums1
            self.recursion(p1+1,p2,nums1,nums2,temp_num,k,ls)

        if p2 < len(nums2):
            # choose curr el from nums2
            self.recursion(p1,p2+1,nums1,nums2,temp_num*10+nums2[p2],k-1,ls)
            # leave curr el from nums2
            self.recursion(p1,p2+1,nums1,nums2,temp_num,k,ls)
        

a = Solution().maxNumber(nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5)
print(a)