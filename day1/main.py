# First challenge: https://adventofcode.com/2024/day/1

# Requirements
# - Receive 2 lists of numbers
# - Find distance between numbers ordered by position
# Lists
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# Result
# 2 + 1 + 0 + 1 + 2 + 5 = 11

def insertOrdered(num_list = [], number = 0):
    length = len(num_list)
    for ix in range(length):
        if num_list[ix] > number:
            num_list.insert(ix, number)
            return
    num_list.append(number)
    

def findDistance(filePath):
    f = open(filePath)
    sorted_list1 = []
    sorted_list2 = []
    for line in f:
        n1, n2 = line.split("   ")
        insertOrdered(sorted_list1, int(n1))
        insertOrdered(sorted_list2, int(n2))
    f.close()
    l = len(sorted_list1)
    response = 0
    for ix in range(l):
        response = response + abs(sorted_list2[ix] - sorted_list1[ix])
    return response

print(findDistance("day1/ex_input.txt"))
print(findDistance("day1/input.txt"))