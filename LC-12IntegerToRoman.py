class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        arabics = [1000, 900,500,400,100,90,50,40,10,9,5,4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X","IX","V","IV","I"]
        res = []
        
        for i in range(len(arabics)):
            while num - arabics[i] >= 0:
                res.append(romans[i])
                num = num - arabics[i]
        return "".join(res)
                