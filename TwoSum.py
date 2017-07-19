import bisect
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsb = sorted(nums);
        flag = 0;
        i = 0;
        endi = len(numsb);
        for i in range(0,len(numsb)):
            if(numsb[i] > target):
                endi = i;
                break;
        for i in range(0,endi):
            checki = bisect.bisect(numsb,target - numsb[i]);
            if(numsb[checki-1] == target - numsb[i] ):
                #if numsb[i]*2 != target:
                flag = 1;
                a = numsb[i];
                break;
        if(flag == 1):
            for i in range(0,len(nums)):
                if(nums[i]==a):
                    aa = i;
                if(nums[i]==target - a):
                    bb = i;
            return [aa,bb];
        else:
            return [0,0];
