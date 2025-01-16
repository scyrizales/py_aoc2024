# Second challenge: https://adventofcode.com/2024/day/2

# Requirements
# - Read a file with a set of values
# - Evaluate each line to see if they comply with: 
#   - in order asc or desc
#   - distance between members is no greater than 3 not lower than 1

# Reasoning 
# - we will have 2 functions:
#   - evaluateLevel will receive a line from file and determine if level is safe by applying conditions
#   - findSafeLevels will read file, pass to evaluateLevel and keep a count of safe levels

order_map = {
    -1: "desc",
    0: "null",
    1: "asc"
}

def evaluateLevel(list = []):
    length = len(list)
    ix = 1
    previous_num = int(list[0])
    current_num = int(list[1])
    difference = current_num - previous_num
    distance = abs(difference)
    previous_ord = order_map[0 if difference == 0 else difference/distance]
    while ix < length:
        current_num = int(list[ix])
        difference = current_num - previous_num
        distance = abs(difference)
        current_order = order_map[0 if difference == 0 else difference/distance]
        if distance < 1 or distance > 3 or current_order != previous_ord:
            return False
        previous_num = current_num
        previous_ord = current_order
        ix = ix + 1
    return True

def findSafeLevels(file_path):
    safe_levels = 0
    file = open(file_path)
    for line in file:
        if evaluateLevel(line.split(" ")):
            safe_levels = safe_levels + 1
    file.close()
    return safe_levels

print(findSafeLevels("day2/ex_input.txt"))
print(findSafeLevels("day2/input.txt"))