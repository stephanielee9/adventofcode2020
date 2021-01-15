#!/usr/bin/env python3
"""
Solution to Day 2 of Advent of Code
"""

__author__ = "Stephanie"
__email__ = "stephanielee@uchicago.edu"

def main():
    with open('day03input.txt', 'r') as f:
        rows = [row.strip() for row in f.readlines()]

    row_count = len(rows)
    row_len = len(rows[0])
    # print(row_count)

    # x = 3
    # y = 1

    # row_pos = 0
    # col_pos = 0

    # tree_count = 0
    # # print(rows[1][1])
    # for i in range(row_count):
    #     row_pos += y
    #     col_pos = (col_pos + 3) % row_len
    #     if row_pos < row_count:
    #         print(rows[row_pos][col_pos])
    #         if rows[row_pos][col_pos] == "#":
    #             tree_count += 1
    # print(tree_count)

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    # slopes = [(3,1)]
    trees_product = 1
    for x,y in slopes:
        row_pos = 0
        col_pos = 0
        tree_count = 0
        while row_pos < row_count-1:
            row_pos += y
            col_pos = (col_pos + x) % row_len
            # print(row_pos, col_pos)
            if rows[row_pos][col_pos] == "#":
                tree_count += 1
        print(tree_count)
        trees_product *= tree_count
     
    print(trees_product)

if __name__ == "__main__":
    main()