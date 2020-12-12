with open("input.txt") as f:
    data = {
        color.rpartition(" bags")[0]: {
            bag_name: int(n) if n.isdigit() else 0
            for bag in bags.split(',') for n, _, bag_name in [bag.rpartition(" bag")[0].strip().partition(' ')]
        }
        for line in f
        for color, _, bags in
        [line.partition('contain')]
    }


def count_inner_bags(bag_name, data):
    total = 0
    contains = data[bag_name]
    for bag, amount in contains.items():
        if amount:
            total += (amount + amount * count_inner_bags(bag, data))
    return total


if __name__ == '__main__':
    print(count_inner_bags("shiny gold", data))
