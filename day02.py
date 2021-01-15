#!/usr/bin/env python3
"""
Solution to Day 2 of Advent of Code
"""

__author__ = "Stephanie"
__email__ = "stephanielee@uchicago.edu"

# import modules
import re

def main():
    with open('day02input.txt', 'r') as f:
        rows = f.readlines()
    
    # part 1
    valid_count = 0
    for row in rows:
        letter = re.findall(r'([a-z])\:', row)[0]
        mini = int(re.findall(r'([0-9]+)\-', row)[0])
        maxi = int(re.findall(r'\-([0-9]+)', row)[0])
        password = re.findall(r'\:\s([a-z]+)', row)[0]
        letter_count = password.count(letter)

        if letter_count >= mini and letter_count <= maxi:
            valid_count += 1
    print(valid_count)

    # part 2
    valid_count2 = 0
    for row in rows:
        position_count=0
        letter = re.findall(r'([a-z])\:', row)[0]
        pos1 = int(re.findall(r'([0-9]+)\-', row)[0])
        pos2 = int(re.findall(r'\-([0-9]+)', row)[0])
        password = re.findall(r'\:\s([a-z]+)', row)[0]
        if password[pos1-1]==letter:
            position_count+=1
        if password[pos2-1]==letter:
            position_count+=1
        if position_count==1:
            valid_count2+=1
    print(valid_count2)

    

# calling main() function
if __name__ == "__main__":
    main()