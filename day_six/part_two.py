from functools import reduce

if __name__ == '__main__':
    total = 0
    with open("input.txt") as f:
        text = f.read()
    groups = text.split("\n\n")
    for group in groups:
        member_answers = [set(m) for m in group.strip().split('\n')]
        common_answers = reduce(set.intersection, member_answers)
        total += len(common_answers)
    print(total)