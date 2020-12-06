with open('input.txt') as f:
    line = next(f)
    size = len(line.strip())
    index = 3
    trees = 0
    while True:
        try:
            line = next(f)
        except StopIteration:
            break
        c = line[index]
        if c == '#':
            trees += 1
        index = (index + 3) % size
print(trees)
