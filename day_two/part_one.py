valid = 0

with open('input.txt') as f:
    for line in f:
        number_range, _, char_and_password = line.partition(' ')
        char, password = char_and_password.split(':')
        n_from, n_to = map(int, number_range.split('-'))
        if n_from <= password.count(char) <= n_to:
            valid += 1

if __name__ == '__main__':
    print(valid)
