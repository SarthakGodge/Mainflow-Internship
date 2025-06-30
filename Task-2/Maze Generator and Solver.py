import random


def create_maze(n, m):
    maze = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        visited[x][y] = True
        maze[x][y] = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < n-1 and 1 <= ny < m-1 and not visited[nx][ny]:
                maze[x + dx//2][y + dy//2] = 1
                dfs(nx, ny)

    dfs(1, 1)
    maze[0][1] = 1  
    maze[n-1][m-2] = 1  
    return maze

def solve_maze(maze):
    n, m = len(maze), len(maze[0])
    path = []
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= m or maze[x][y] == 0 or visited[x][y]:
            return False
        visited[x][y] = True
        path.append((x, y))
        if (x, y) == (n-1, m-2):
            return True
        if dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x, y-1):
            return True
        path.pop()
        return False

    dfs(0, 1)
    return path

def display_maze(maze, path=None):
    for i, row in enumerate(maze):
        line = ''
        for j, cell in enumerate(row):
            if path and (i, j) in path:
                line += '.'
            elif cell == 1:
                line += ' '
            else:
                line += '#'
        print(line)

if __name__ == "__main__":
    width, height = 21, 21  
    maze = create_maze(height, width)
    print("Generated Maze:\n")
    display_maze(maze)

    print("\nSolved Maze Path:\n")
    path = solve_maze(maze)
    display_maze(maze, path)
