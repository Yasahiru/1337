

def create_grid(size: int) -> list[str]:
    grid = []
    i = 0
    while i < size:
        grid.append("."*size)
        i += 1
    return grid

def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    grid = create_grid(dim)
    for x,y in stars:
        if x > dim or y > dim:
            continue
        grid[x] = grid[x][:y] + "*" + grid[x][y+1:]
    return grid

res = [
    (constellation_mapper([(0, 0), (1, 1), (2, 2)], 3), ['*..', '.*.', '..*']),
    (constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3), ['.*.', '***', '.*.']),
    (constellation_mapper([], 2), ['..', '..']),
    (constellation_mapper([(0, 0), (0, 0), (1, 1)], 2), ['*.', '.*']),
    (constellation_mapper([(0, 0), (5, 5)], 3), ['*..', '...', '...']),
    (constellation_mapper([(1, 0), (1, 1), (1, 2)], 3), ['...', '***', '...'])
]

for r, a in res:
    print(r == a)
