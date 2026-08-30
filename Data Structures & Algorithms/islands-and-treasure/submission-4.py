class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        chest_queue = deque()
        
        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            chest_queue.append([r, c])


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    chest_queue.append((r,c))
                    visit.add((r,c))
        dist = 0

        while chest_queue:
            for i in range(len(chest_queue)):
                r,c = chest_queue.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

            
            
            











        