from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        matrix = [row[:] for row in mat]
        m = len(matrix)
        n = len(matrix[0])
        queue = deque()
        seen = set()
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0))
                    seen.add((row, col))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, steps = queue.popleft()
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if (next_row, next_col) not in seen and valid(next_row, next_col):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                    matrix[next_row][next_col] = steps + 1
        
        return matrix