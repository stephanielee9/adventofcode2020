#!/usr/bin/env python3
"""
Solution to Day 1 of Advent of Code
"""

__author__ = "Stephanie"
__email__ = "stephanielee@uchicago.edu"

def main():
    with open('day01input.txt', 'r') as f:
        entries = f.read().split()

    # print(entries)
    entries_num = list(map(lambda x:int(x), entries))
    # print(entries_num)

    sum_2020 = []
    for num1 in entries_num:
        for num2 in entries_num:
            if num1 + num2 == 2020:
                if num1 not in sum_2020 and num2 not in sum_2020:
                    sum_2020.append(num1)
                    sum_2020.append(num2)

    # print(sum_2020)
    product_2020 = sum_2020[0]*sum_2020[1]
    print(product_2020)

    sum_2020 = []
    for num1 in entries_num:
        for num2 in entries_num:
            for num3 in entries_num:
                if num1 + num2 + num3 == 2020:
                    if num1 not in sum_2020 and num2 not in sum_2020 and num3 not in sum_2020:
                        sum_2020.append(num1)
                        sum_2020.append(num2)
                        sum_2020.append(num3)

    print(sum_2020)
    product_2020 = sum_2020[0]*sum_2020[1]*sum_2020[2]
    print(product_2020)

# calling main() function
if __name__ == "__main__":
    main()