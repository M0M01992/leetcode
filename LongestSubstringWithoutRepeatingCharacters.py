class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = 0;
        maxlen = 0;
        chhash = [-1 for x in range(256)];
        
        for i in range(0,len(s)):
            if(chhash[ord(s[i])] == -1 or chhash[ord(s[i])] < start):
                maxlen = max(maxlen, i-start+1);
            else:
                start = chhash[ord(s[i])]+1;
            
            chhash[ord(s[i])]=i;
            
            
            
        return maxlen;
