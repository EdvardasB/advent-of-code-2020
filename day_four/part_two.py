import re
from functools import wraps
from typing import Dict

hair_color_pattern = re.compile("#[0-9a-f]{6}$")


def passport_validator(f):
    @wraps(f)
    def wrapper(passport):
        try:
            is_valid = f(passport)
        except:
            return False
        return is_valid

    return wrapper


@passport_validator
def is_valid_birth_year(passport: Dict[str, str]):
    """
    >>> is_valid_birth_year({"byr":"1919"})
    False
    >>> is_valid_birth_year({"byr":"1920"})
    True
    >>> is_valid_birth_year({"byr":"2002"})
    True
    >>> is_valid_birth_year({"byr":"2003"})
    False
    >>> is_valid_birth_year({"byr":"sadas"})
    False

    :param passport: Dict[str,str]
    :return:
    """
    return 1920 <= int(passport["byr"]) <= 2002


@passport_validator
def is_valid_issue_year(passport: Dict[str, str]):
    """
    >>> is_valid_issue_year({"iyr":"2009"})
    False
    >>> is_valid_issue_year({"iyr":"2010"})
    True
    >>> is_valid_issue_year({"iyr":"2020"})
    True
    >>> is_valid_issue_year({"iyr":"2021"})
    False
    >>> is_valid_issue_year({"iyr":"sadas"})
    False

    :param passport: Dict[str,str]
    :return:
    """
    return 2010 <= int(passport["iyr"]) <= 2020


@passport_validator
def is_valid_expiration_year(passport: Dict[str, str]):
    """
    >>> is_valid_expiration_year({"eyr":"2019"})
    False
    >>> is_valid_expiration_year({"eyr":"2020"})
    True
    >>> is_valid_expiration_year({"eyr":"2030"})
    True
    >>> is_valid_expiration_year({"eyr":"2031"})
    False
    >>> is_valid_expiration_year({"eyr":"sadas"})
    False

    :param passport: Dict[str,str]
    :return:
    """
    return 2020 <= int(passport["eyr"]) <= 2030


@passport_validator
def is_valid_height(passport: Dict[str, str]):
    """
    >>> is_valid_height({"hgt":"60in"})
    True
    >>> is_valid_height({"hgt":"190cm"})
    True
    >>> is_valid_height({"hgt":"190in"})
    False
    >>> is_valid_height({"hgt":"190"})
    False

    :param passport:
    :return:
    """
    height = passport["hgt"]
    n = int(height[:-2])
    units = height[-2:]
    if units == "cm" and 150 <= n <= 193:
        return True
    if units == "in" and 59 <= n <= 76:
        return True
    return False


@passport_validator
def is_valid_hair_color(passport: Dict[str, str]):
    """
    >>> is_valid_hair_color({"hcl":"#123abc"})
    True
    >>> is_valid_hair_color({"hcl":"#123abz"})
    False
    >>> is_valid_hair_color({"hcl":"123abc"})
    False

    :param passport:
    :return:
    """
    hair_color_pattern = re.compile("#[0-9a-f]{6}$")
    return bool(hair_color_pattern.match(passport['hcl']))


@passport_validator
def is_valid_eye_color(passport: Dict[str, str]):
    """
    >>> is_valid_eye_color({"ecl":"brn"})
    True
    >>> is_valid_eye_color({"ecl":"wat"})
    False

    :param passport:
    :return:
    """
    return passport['ecl'] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


@passport_validator
def is_valid_passport_id(passport: Dict[str, str]):
    """
    >>> is_valid_passport_id({"pid":"000000001"})
    True
    >>> is_valid_passport_id({"pid":"0123456789"})
    False

    :param passport:
    :return:
    """
    pid_ = passport['pid']
    return pid_.isnumeric() and len(pid_) == 9


VALIDATORS = [
    is_valid_birth_year,
    is_valid_issue_year,
    is_valid_expiration_year,
    is_valid_height,
    is_valid_hair_color,
    is_valid_eye_color,
    is_valid_passport_id
]


def is_valid(passport: Dict[str, str]):
    return all([validator(passport) for validator in VALIDATORS])


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
