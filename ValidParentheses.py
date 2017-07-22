class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = [];
        for i in range(len(s)):
            if(s[i] == '(' or s[i] == '[' or s[i] == '{'):
                stack.append(s[i]);
            elif(s[i] == ')'):
                if(len(stack) == 0):
                    return False;
                elif(stack[-1] == '('):
                    stack.pop();
                else:
                    return False;
            elif(s[i] == ']'):
                if(len(stack) == 0):
                    return False;
                elif(stack[-1] == '['):
                    stack.pop();
                else:
                    return False;
            elif(s[i] == '}'):
                if(len(stack) == 0):
                    return False;
                elif(stack[-1] == '{'):
                    stack.pop();
                else:
                    return False;
        if(len(stack)!=0):
            return False;
        return True;
