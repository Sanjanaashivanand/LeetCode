class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        rows = {}
        cols = {}

        for i in range(0, n):
            row = []
            col = []

            for j in range(0,n):
                row.append(grid[i][j])
                col.append(grid[j][i])

            if tuple(row) not in rows:
                rows[tuple(row)] = 0
            rows[tuple(row)]+=1

            if tuple(col) not in cols:
                cols[tuple(col)] = 0
            cols[tuple(col)] += 1

        return sum(rows[k] * cols[k] for k in rows if k in cols)




