class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        parentheses = {')' : '(', ']':'[', '}':'{'}

        for i in s:
            if not i in parentheses.keys():
                stack.append(i)
            elif (len(stack)!=0):
                temp = stack.pop()
                if temp!=parentheses[i]:
                    return False
            else:
                return False
        
        return len(stack) == 0
