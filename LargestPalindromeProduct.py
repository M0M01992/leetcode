#---------------Not Accepted Yet----------------#
import urllib
def isPalindrome(n):
    strn = str(n);
    if(strn == "".join(reversed(strn))):
        return True;
    return False;

def largestPalindrome(n):
    """
    :type n: int
    :rtype: int
    """

    for i in range(pow(10,n)-1 , pow(10,n-1)-1,-1):
        for j in range(i, pow(10,n-1)-1,-1):
            num = i*j;
            if(isPalindrome(num)):
                print(num);
                return num%1337;
    return 0;
