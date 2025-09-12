class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        value_mapping = {1: 'I', 5:'V', 10: 'X', 50:'L', 100: 'C', 500: 'D', 1000:'M'}

        i=0
        returnable=""
        while num!=0:
            temp = num%10
            num = (num-temp)//10
            if (temp==4):
                returnable = value_mapping[10**i] + value_mapping[5*10**i] + returnable
                pass
            elif (temp==9):
                returnable = value_mapping[10**i]+ value_mapping[10**(i+1)] + returnable
                pass
            else:
                if (temp<5):
                    returnable=value_mapping[10**i]*temp +returnable
                else:
                    returnable=value_mapping[10**i*5] + value_mapping[10**i] * (temp-5)+returnable
                
            i+=1

        return returnable
        