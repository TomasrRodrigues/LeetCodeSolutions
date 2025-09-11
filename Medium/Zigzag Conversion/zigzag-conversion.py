class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        
        astring = ""
        step = 0
        # row by row, the step between a letter and the following in the same line is 
        # 2*(numRows-currentRow-1)
        for i in range(numRows):
            temp = i
            step1 = 2 * (numRows - i - 1)
            step2 = 2 * i
            toggle = True
            
            while temp < len(s):
                astring += s[temp]

                # If step1 or step2 is 0 then we are either in the first or in the last row
                if (toggle and step1!=0):
                    temp+=step1
                elif (not toggle and step2!=0):
                    temp+=step2
                else:
                    # First and Last Rows
                    temp += step1 if step1 != 0 else step2
                toggle = not toggle
        return astring

        