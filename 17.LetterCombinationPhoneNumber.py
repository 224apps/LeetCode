class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phoneMap = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7' : 'pqrs', '8': 'tuv', '9':'wxyz'}
        number = str(digits)
        
        if number  == "":
            return []
        result = ['']
        for char in number:
            values = phoneMap[char]
            newResult = []
            for prefix in result:
                currElement = prefix
                for value in values:
                    newResult.append(currElement + value)
            result = newResult
        return result
     