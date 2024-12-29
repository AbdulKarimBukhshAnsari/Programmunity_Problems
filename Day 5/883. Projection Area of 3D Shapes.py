class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
    
        top = 0 
        front = 0 
        side = 0
        top = sum(1 for row in grid for cell in row if cell > 0)
        side = sum(max(grid[i]) for i in range(len(grid)))
        for i in range(len(grid)):
            max_element = 0 
            for j in range(len(grid)):
                max_element = max(grid[j][i], max_element)
            front+= max_element
        return top+front+side
