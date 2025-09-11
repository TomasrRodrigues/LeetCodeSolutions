class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        beginning=True
        returnable_string=""
        negative=False

        for i in s:
            if beginning:
                if i==' ':
                    pass
                elif i=='-':
                    negative=True
                    beginning=False
                    pass
                elif i.isdigit():
                    returnable_string+=i
                    beginning=False
                    pass
                elif i=='+':
                    beginning=False
                else:
                    return 0
            else:
                if not i.isdigit():
                    break
                returnable_string+=i
        
        if len(returnable_string)==0: return 0
        if negative: 
            returnable_string = "-" + returnable_string
        
        if (int(returnable_string)<-2**31):
            return -2**31
        elif (int(returnable_string)>2**31-1):
            return 2**31-1
        
        return int(returnable_string)


