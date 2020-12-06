with open('input.txt') as f:
    lines = list(f)


def check_slope(lines, shift_right, shift_down):
    line = next(lines)
    size = len(line.strip())
    index = shift_right
    trees = 0
    while True:
        try:
            for _ in range(shift_down):
                line = next(lines)
        except StopIteration:
            break
        c = line[index]
        if c == '#':
            trees += 1
        index = (index + shift_right) % size
    return trees


n1 = check_slope(iter(lines), 1, 1)
print(n1)
n2 = check_slope(iter(lines), 3, 1)
print(n2)
n3 = check_slope(iter(lines), 5, 1)
print(n3)
n4 = check_slope(iter(lines), 7, 1)
print(n4)
n5 = check_slope(iter(lines), 1, 2)
print(n5)
print(n1 * n2 * n3 * n4 * n5)
