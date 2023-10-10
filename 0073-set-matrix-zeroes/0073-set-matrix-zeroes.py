class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        row, col = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)
        
        for r in range(rows):
            for c in range(cols):
                if r in row or c in col:
                    matrix[r][c] = 0
                    