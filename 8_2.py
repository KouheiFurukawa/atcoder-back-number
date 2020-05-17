already_visited = {(1, 0) : 1}
m = 10
n = 10

def get_path(x, y, path):
    if x == n - 1 and y == m - 1:
        path.append((y, x))
        return path
    path.append((y, x))
    already_visited[(y, x)] = 1
    if x < n - 1 and (x + 1, y) not in already_visited:
        return get_path(x + 1, y, path)
    if y < m - 1 and (x, y + 1) not in already_visited:
        return get_path(x, y + 1, path)
    return False

print(get_path(0, 0, []))