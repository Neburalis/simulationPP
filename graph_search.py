from collections import deque


def bfs_path(graph: list[list[int | str]], start: tuple[int, int], goal: str) -> list[tuple[int, int]] | None:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque([(start, [])])
    visited = {start}

    rows, cols = len(graph), len(graph[0])

    while queue:
        (current_x, current_y), path = queue.popleft()

        for direction in directions:
            next_x, next_y = current_x + direction[0], current_y + direction[1]

            if 0 <= next_x < rows and 0 <= next_y < cols and (next_x, next_y) not in visited:
                if graph[next_x][next_y] == goal:
                    return path + [direction]
                elif graph[next_x][next_y] == 0:
                    queue.append(((next_x, next_y), path + [direction]))
                    visited.add((next_x, next_y))

    return None
