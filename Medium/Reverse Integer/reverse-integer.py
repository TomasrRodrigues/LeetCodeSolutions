class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x>=0):
            x= str(x)[::-1]
            returnable = x
        else :
            x = str(x)[1::]
            x= x[::-1]
            returnable = "-" + x
            
        if (int(returnable)<(-2**31) or int(returnable)>(2**31-1)): return 0

        return int(returnable)
            