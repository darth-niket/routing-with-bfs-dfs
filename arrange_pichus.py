#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : Niket Malihalli
#
# Based on skeleton code in CSCI B551, Fall 2021.
import sys
# import numpy as np
# Parse the map from a given filename
def parse_map(filename):
   with open(filename, "r") as f:
      return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

#Check for pichu in right side. Return True if no Pichu is present. Return False if pichu is present
def check_right(house_map, row, col):
    while col < len(house_map[0]):
        if house_map[row][col] == 'p':
            return False
        elif house_map[row][col] == 'X' or house_map[row][col] == '@':
            break
        else:
            col = col+1
    return True

#Check for pichu on left side. Return True if no Pichu is present. Return False if pichu is present
def check_left(house_map, row, col):
    while col>=0:
        if house_map[row][col]=='p':
            return False
        elif house_map[row][col]=='X' or house_map[row][col]=='@':
            break
        else:
            col=col-1
    return True

#Check for pichu upwards. Return True if no Pichu is present. Return False if pichu is present
def check_up(house_map, row, col):
    while row>=0:
        if house_map[row][col]=='p':
            return False
        elif house_map[row][col]=='X' or house_map[row][col]=='@':
            break
        else:
            row=row-1
    return True

#Check for pichu in downwards. Return True if no Pichu is present. Return False if pichu is present
def check_down(house_map, row, col):
    while row < len(house_map):
        if house_map[row][col]=='p':
            return False
        elif house_map[row][col]=='X' or house_map[row][col]=='@':
            break
        else:
            row=row+1
    return True

#Check for pichu in north-west direction. Return True if no Pichu is present. Return False if pichu is present
def check_nw_diag(house_map, row, col):
    while row>=0 and col>=0:
        if house_map[row][col]=='p':
            return False
        elif house_map[row][col]=='X' or house_map[row][col]=='@':
            break
        else:
            row=row-1
            col=col-1
    return True

#Check for pichu in north-east direction. Return True if no Pichu is present. Return False if pichu is present
def check_ne_diag(house_map, row, col):
    while row>=0 and col<len(house_map[0]):
        if house_map[row][col]=='p':
            return False
        elif house_map[row][col]=='X' or house_map[row][col]=='@':
            break
        else:
            row=row-1
            col=col+1
    return True

#Check for pichu in south-east direction. Return True if no Pichu is present. Return False if pichu is present
def check_se_diag(house_map, row, col):
    while row<len(house_map) and col<len(house_map[0]):
        if house_map[row][col]=='p':
            return False
        elif house_map[row][col]=='X' or house_map[row][col]=='@':
            break
        else:
            row=row+1
            col=col+1
    return True

#Check for pichu in south-west direction. Return True if no Pichu is present. Return False if pichu is present
def check_sw_diag(house_map, row, col):
    while row<len(house_map) and col>=0:
        if house_map[row][col]=='p':
            return False
        elif house_map[row][col]=='X' or house_map[row][col]=='@':
            break
        else:
            row=row+1
            col=col-1
    return True

#Return True if Pichu is safe to place.
def is_safe(house_map, row, col):
    return check_down(house_map, row, col) and check_up(house_map, row, col)and check_right(house_map, row, col)\
        and check_left(house_map, row, col) and check_ne_diag(house_map, row, col) and check_nw_diag(house_map, row, col)\
             and check_se_diag(house_map, row, col) and check_sw_diag(house_map, row, col)


# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' ]


# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    if is_safe(house_map, row, col):
        return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]
    else:
        return house_map[0:row] + [house_map[row][0:col] + ['.', ] + house_map[row][col + 1:]] + house_map[row + 1:]

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#

def solve(initial_house_map,k):
    fringe = [initial_house_map]
    visited = []
    while len(fringe) > 0:
        visited.append(fringe[-1])
        for new_house_map in successors(fringe.pop()):
            if new_house_map in visited:
                continue
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)
    return(new_house_map, False)
# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")
