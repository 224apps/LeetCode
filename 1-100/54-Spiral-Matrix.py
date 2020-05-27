class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiralList = []

        if not matrix:
            return  spiralList
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right =len(matrix[0]) - 1
        direction = "right"

        while top <= bottom and left <= right:
            if direction == "right":
                for i in range(left, right + 1):
                    spiralList.append(matrix[top][i])
                top += 1
                direction = "down"
            elif direction =="down" :
                for i in range(top, bottom + 1):
                    spiralList.append(matrix[i][right])
                right -= 1
                direction = "left"
            elif direction == "left":
                for i in range(right, left - 1, -1):
                    spiralList.append(matrix[bottom][i])
                bottom -= 1
                direction ="up"
            elif direction == "up":
                for i in range(bottom, top - 1, -1 ):
                    spiralList.append(matrix[i][left])
                left += 1
                direction = "right"
        return spiralList

        
        
                    
                
        