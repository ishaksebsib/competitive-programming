class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i,j=0,0
        if not matrix:
            return matrix
        m,n = len(matrix),len(matrix[0])
        arr = []
        while i<m and j<n:
                
            for k in range(j,n):
                arr.append(matrix[i][k])
            
            for k in range(i+1,m):
                arr.append(matrix[k][n-1])
            if i+1<m:
                for k in range(n-2,j-1,-1):
                    arr.append(matrix[m-1][k])
                    
            if j+1<n:   
                for k in range(m-2,i,-1):
                    arr.append(matrix[k][j])
            i+=1
            j+=1
            m-=1
            n-=1
        return  arr
