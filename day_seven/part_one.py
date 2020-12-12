with open("input.txt") as f:
    data = {
        color.rpartition(" bags")[0]: {
            bag.rpartition(" bag")[0].strip().partition(' ')[2]
            for bag in bags.split(',')
        }
        for line in f
        for color, _, bags in
        [line.partition('contain')]
    }


def find_outer_bag_for(bag_name, data):
    for bag, contains in data.items():
        if bag_name in contains:
            yield bag
            yield from find_outer_bag_for(bag, data)


if __name__ == '__main__':
    g = find_outer_bag_for("shiny gold", data)
    bags = set(g)
    print(len(bags))
