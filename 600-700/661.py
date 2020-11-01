'''
661. Image Smoother
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
'''

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        results = []
        cols = len(M[0])
        rows = len(M)
        
        for r, row in enumerate(M):
            results.append([])
            for c, col in enumerate(row):
                s = 0
                count = 0
                for dx in  range(-1, 2):
                    for dy in range(-1, 2):
                        if 0 <= r + dx < rows and 0 <= c + dy < cols:
                            s += M[r+dx][c + dy]
                            count += 1
                results[-1].append(s // count)
        return results
                    