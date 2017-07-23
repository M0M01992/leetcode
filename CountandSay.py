class Solution(object):
    def count(self,strn,loc,goal):
        count = 0;
        while(loc < len(strn) and strn[loc] == goal):
            count = count + 1;
            loc = loc + 1;
        return count;
    def nextstr(self,strn):
        ans = "";
        i = 0;
        while(i < len(strn)):
            time = self.count(strn,i,strn[i]);
            ans = ans + str(time) + strn[i];
            i = i + time;
        return ans;

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if(n == 1):
            return "1";
        else:
            strn = "1";
            for i in range(1,n):
                strn = self.nextstr(strn);
        
        return strn;
