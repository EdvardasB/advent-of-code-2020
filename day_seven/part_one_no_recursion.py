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


if __name__ == '__main__':
    bags = set()
    to_check = ["shiny gold"]
    while to_check:
        temp_to_check = []
        for unchecked_bag_name in to_check:
            g = find_outer_bag_for(unchecked_bag_name, data)
            for bag_name in g:
                if bag_name in bags:
                    continue
                temp_to_check.append(bag_name)
                bags.add(bag_name)
        to_check = temp_to_check

    print(len(bags))
