if __name__ == '__main__':
    with open("input.txt") as f:
        answer_count = sum([len(set(group.replace('\n', ''))) for group in f.read().split("\n\n")])
    print(answer_count)
