valid = 0

with open('input.txt') as f:
    for line in f:
        indexes, _, char_and_password = line.partition(' ')
        char, password = char_and_password.split(':')
        i, i2 = map(int, indexes.split('-'))
        password = password.strip() + " " * 10
        if (password[i - 1] == char or password[i2 - 1] == char) and password[i - 1] != password[i2 - 1]:
            valid += 1

if __name__ == '__main__':
    print(valid)
