class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        firstColZero = False
        firstRowZero  = False

        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                firstColZero = True
                break
        
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                firstRowZero = True
                break
        
        #use first rown and col as flags
        for row in range(1, len(matrix)):
            for col  in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1, len(matrix)):
            for col  in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if firstColZero:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0
        
        if firstRowZero:
            for j in range(0, len(matrix[0])):
                matrix[0][j] = 0



