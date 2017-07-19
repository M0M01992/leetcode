import urllib
import bisect
def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numsb = sorted(nums);
    flag = 0;
    i = 0;
    for i in range(0,len(numsb)):
        checki = bisect.bisect(numsb,target - numsb[i]);
        if(numsb[checki-1] == target - numsb[i] ):
            flag = 1;
            a = numsb[i];
            break;
    if(flag == 1):
        for i in range(0,len(nums)):
            if(nums[i]==a or nums[i] == target - a):
                aa = i;
                a = nums[i];
                for j in range(i+1, len(nums)):
                    if(nums[j]==target - a):
                        bb = j;
                break;

        return sorted([aa,bb]);
    else:
        return [0,0];
