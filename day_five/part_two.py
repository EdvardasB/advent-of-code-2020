from day_five.part_one import code_to_seat

if __name__ == '__main__':
    with open("input.txt") as f:
        ids = sorted(map(code_to_seat, f))

    for i, ii in zip(ids[:-1], ids[1:]):
        if ii - i == 2:
            print(i + 1)
