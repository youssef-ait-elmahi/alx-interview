def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (List[List[int]]): A 2D list of integers where 0 represents
        water and 1 represents land.

    Returns:
        int: The perimeter of the island.

    This function works by iterating over each cell in the grid. If the cell
    is land (1),it checks the four directions (up, down, left, right). If any
    of these directions is either water (0) or out of the grid boundaries, it
    adds 1 to the perimeter count.
    """
    rows = len(grid)
    cols = len(grid[0])

    result = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r-1][c] == 0:
                    result += 1
                if r == rows-1 or grid[r+1][c] == 0:
                    result += 1
                if c == 0 or grid[r][c-1] == 0:
                    result += 1
                if c == cols-1 or grid[r][c+1] == 0:
                    result += 1

    return result
