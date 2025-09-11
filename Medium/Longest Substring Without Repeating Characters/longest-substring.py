class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # If string is "" return 0
        if s=="":
            return 0
        max_size=1
        temp_string=s[0]

        for i in range(1,len(s)):
            # If the next char is not in the temp string yet add it
            if s[i] not in temp_string:
                temp_string+=s[i]
            else:
                # If it is, update the max size
                if (max_size<len(temp_string)): 
                    max_size = len(temp_string)
                
                # While the char is still in the temp string remove the first element 
                while (s[i] in temp_string):
                    temp_string=temp_string[1:]
                    
                temp_string+=s[i]
        
        return max(max_size, len(temp_string))
