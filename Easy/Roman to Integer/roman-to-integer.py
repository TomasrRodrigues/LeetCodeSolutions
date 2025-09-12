class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_mapping = {'I': 1, 'V':5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M':1000}
        i=0
        rsum=0
        while i<len(s):
            if (i+1<len(s) and value_mapping[s[i]] < value_mapping[s[i+1]]):
                rsum += value_mapping[s[i+1]] - value_mapping[s[i]]
                i+=2
            else:
                rsum+=value_mapping[s[i]]
                i+=1

            
        return rsum

