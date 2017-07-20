class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.strip();
        i = 0;
        flag = 0;
        flagpoint = 0;
        if (s == "" or s == " "):
            return False;
        if(s[0] == 'e'):
            return False;
        for i in range(len(s)):
            if(s[i] == 'e'):
                flag = 1;
                break;
        if(flag == 1):
            Bnum = s[0:i];
            if(i == len(s)-1):
                return False;
            Inum = s[i+1:];
            if(Bnum[0] == '+' or Bnum[0] == '-'):
                Bnum = Bnum[1:];
            if(Inum[0] == '+' or Inum[0] == '-'):
                Inum = Inum[1:];
            if(Bnum == '' or Inum == '' or Bnum == '.'):
                return False;

            i = 0;
            j = 0;
            for i in range(len(Bnum)):
                if(Bnum[i] == '.' and flagpoint == 0):
                    flagpoint = 1;
                elif(Bnum[i]>'9' or Bnum[i]<'0'):
                    return False;
            for j in range(len(Inum)):
                if(Inum[j]>'9' or Inum[j]<'0'):
                    return False;

        else:
            Bnum = s;
            i = 0;
            if(Bnum[0] == '+' or Bnum[0] == '-'):
                Bnum = Bnum[1:];
            if(Bnum == '' or Bnum == '.'):
                return False;
            for i in range(len(Bnum)):
                if(Bnum[i] == '.' and flagpoint == 0):
                    flagpoint = 1;
                elif(Bnum[i]>'9' or Bnum[i]<'0'):
                    return False;

        return True;
