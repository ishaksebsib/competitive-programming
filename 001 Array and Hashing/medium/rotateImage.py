# LINK : https://leetcode.com/problems/rotate-image/ 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        res = []
        length = len(matrix)
        
        for i in range(length):
            row = []
            for j in range(length):
                row.append(matrix[j][i])
            res.append(row[::-1])
        
        matrix[:] = res
            

        
