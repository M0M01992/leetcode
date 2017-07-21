class Solution(object):
    def check(self,box,row):
        if(row == 0):
            return True;
        for i in range(row):
            if(box[row] == box[i] or abs(row - i)==abs(box[row] - box[i])):
                return False;
        return True;
    
    def printans(self,ans,n):
        Qans = [["" for i in range(n)] for j in range(len(ans))];
        for i in range(len(ans)):
            for j in range(n):
                for k in range(n):
                    if(ans[i][j] == k):
                        Qans[i][j] = Qans[i][j] + 'Q';
                    else:
                        Qans[i][j] = Qans[i][j] + '.'

        return Qans;
            
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = [];
        box = [-1 for i in range(n)];
        row = 0;
        col = 0;
        while(row >= 0):
            col = box[row] + 1;
            if(col == n):
                row = row - 1;
                for i in range(row+1,n):
                    box[i] = -1;
            else:
                while(col < n):
                    tmp = box[row];
                    box[row]=col;
                    if(self.check(box,row)):
                        row = row + 1; #找到该行的一个可行列，开始判断下一行
                        if(row == n): #已找到一组可行解，同时回撤到上一行
                            thisbox = [-1 for i in range(n)];
                            for i in range(n):
                                thisbox[i] = box[i];
                            ans.append(thisbox);
                            row = row - 1;
                        break;
                    else:
                        box[row] = tmp;
                        col = col + 1;
                        if(col == n):
                            row = row - 1;
                            for i in range(row+1,n):
                                box[i] = -1;
                            break;

        return self.printans(ans,n);
