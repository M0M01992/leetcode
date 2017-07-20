class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0;
        if(len(s) == 0):
            return "";
        if(len(s) == 1):
            return s;

        for i in range(len(s)):
            j=i-1;
            k=i+1;
            thissinglen = 1;
            while(j>=0 and k <=len(s)-1 and s[j] == s[k]):
                thissinglen = thissinglen + 2;
                j = j - 1;
                k = k + 1;
            singstart = j+1;
            singend = k-1;
            thisdoublen = 0;
            if(i<len(s)-1 and s[i] == s[i+1]):
                thisdoublen = 2;
                j = i-1;
                k = i+2;
                while(j >=0 and k<=len(s)-1 and s[j] == s[k]):
                    thisdoublen = thisdoublen + 2;
                    j = j - 1;
                    k = k + 1;
                doubstart = j + 1;
                doubend = k - 1;

            if(thissinglen > maxlen):
                start = singstart;
                end = singend;
                maxlen = thissinglen;
            if(thisdoublen > maxlen):
                start = doubstart;
                end = doubend;
                maxlen = thisdoublen;

        return s[start:end+1]
