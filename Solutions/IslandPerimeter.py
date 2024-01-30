class IslandPerimeter:
    def island_perimeter(self, grid):
        perimeter = 0
        rows = len(grid)
        columns = len(grid[0])

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
        return perimeter


s = IslandPerimeter()
print(s.island_perimeter([[1, 1, 1, 1],
                          [1, 1, 1, 1],
                          [1, 1, 1, 1],
                          [1, 1, 1, 1]]))
