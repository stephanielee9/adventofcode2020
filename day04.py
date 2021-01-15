#!/usr/bin/env python3
"""
Day04.py: Day 4 of 2020 Advent of Code
"""

__author__ = "Stephanie Lee"
__email__ = "stephanielee@uchicago.edu"

# import modules
import re

# declaring global constants (in caps)

# main function when module used as a standalone script
def main():
    with open('day04input.txt', 'r') as f:
        passports = f.read().split('\n\n')
    
    # print(text)

    # passports = re.findall(r'([\w\W]+)\n\n', text)
    # print(passports)
    required_fields = 'byr iyr eyr hgt hcl ecl pid'.split()
    # print(required_fields)

    valid_passports = 0
    for passport in passports:
        field_count = 0
        for field in required_fields:
            if field in passport:
                field_count +=1
        if field_count ==7:
            valid_passports += 1
    print(valid_passports)


# calling main() function
if __name__ == "__main__":
    main()