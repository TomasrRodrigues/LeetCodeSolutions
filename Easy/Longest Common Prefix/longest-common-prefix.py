class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # Having it sorted alphabetically, if the first and the last one have the same 
        # prefix, the ones in the middle have the same too 
        strs.sort()

        prefix=""
        for i in range(min(len(strs[0]), len(strs[len(strs)-1]))):
            if (strs[0][i] != strs[len(strs) - 1][i]):
                return prefix
            prefix+=strs[0][i]
        
        return prefix