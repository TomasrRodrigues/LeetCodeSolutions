class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(i, path):
            if i == len(digits):
                res.append("".join(path))
                return
            
            for ch in mapping[digits[i]]:
                path.append(ch)
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        return res