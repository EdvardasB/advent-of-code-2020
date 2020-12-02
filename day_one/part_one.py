with open("input.txt") as f:
    data = set(map(int, f))

for n in data:
    match_diff = 2020 - n
    if match_diff in data:
        break

if __name__ == '__main__':
    print(n, match_diff)
    print(n * match_diff)