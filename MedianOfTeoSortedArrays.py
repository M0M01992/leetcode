class Solution:
    def findKmin(self,nums1,len1,i1,nums2,len2,i2,kmin):
        if(len1-i1 > len2-i2):
            return self.findKmin(nums2,len2,i2,nums1,len1,i1,kmin);
        if(len1-i1 == 0):
            return nums2[i2+kmin-1];
        if(kmin == 1):
            return min(nums1[i1],nums2[i2]);

        p1 = min(len1-i1,int(kmin/2));
        p2 = kmin - p1;

        if(nums1[i1+p1-1]<nums2[i2+p2-1]):
            return self.findKmin(nums1,len1,i1+p1,nums2,len2,i2,kmin-p1);
        elif(nums1[i1+p1-1]>nums2[i2+p2-1]):
            return self.findKmin(nums1,len1,i1,nums2,len2,i2+p2,kmin-p2);
        else:
            return nums1[i1+p1-1];
        
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1);
        len2 = len(nums2);
        total = len1 + len2

        if( total%2 == 1):
            return float(self.findKmin(nums1,len1,0,nums2,len2,0,int((total+1)/2)));
        else:
            return (self.findKmin(nums1,len1,0,nums2,len2,0,int(total/2)) + self.findKmin(nums1,len1,0,nums2,len2,0,int(total/2+1)))/2;
