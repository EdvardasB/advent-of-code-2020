def is_valid(passport):
    mandatory = {"byr", 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return mandatory.issubset(set(passport))


with open("input.txt") as f:
    valid = 0
    passport = {}
    for line in f:
        if not line.strip():
            valid += is_valid(passport)
            passport = {}
            continue
        passport.update({k: v for val in line.strip().split() for k, v in [val.split(":")]})
    if passport:
        valid += is_valid(passport)
print(valid)