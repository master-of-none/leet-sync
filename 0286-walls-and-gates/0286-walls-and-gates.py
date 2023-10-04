class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])
        visit = set()
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist = 0

        def addRoom(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or rooms[r][c] == -1 or (r, c) in visit:
                return
            visit.add((r,c))
            q.append([r,c])
        

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)

            dist += 1
    