with open("input.txt") as f:
    data = set(map(int, f))


# O(n2) complexity
def find_pairs(number_sum, numbers, depth):
    for n in numbers:
        diff = number_sum - n
        if depth > 0:
            values = find_pairs(diff, numbers, depth - 1)
            if values:
                return [n] + values
        else:
            if diff in numbers:
                return [n, diff]


if __name__ == '__main__':
    a, b, c = find_pairs(2020, data, 1)
    print(a, b, c)
    print(a * b * c)
