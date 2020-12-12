with open("input.txt") as f:
    data = {
        color.rpartition(" bags")[0]: [
            (bag_name, int(n) if n.isdigit() else 0)
            for bag in bags.split(',') for n, _, bag_name in [bag.rpartition(" bag")[0].strip().partition(' ')]
        ]
        for line in f
        for color, _, bags in
        [line.partition('contain')]
    }


def expand(bag, data):
    to_expand = data[bag]
    expanded = sum(x[1] for x in to_expand)
    while to_expand:
        bag_name, parent_count = to_expand.pop()
        if bag_name in data:
            for name, count in data[bag_name]:
                total_count_for_bag = count * parent_count
                expanded += total_count_for_bag
                to_expand.append((name, total_count_for_bag))
    return expanded


if __name__ == '__main__':
    print(expand("shiny gold", data))
