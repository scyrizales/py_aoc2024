# Third challenge: https://adventofcode.com/2024/day/3

# Requirements:
# - Read a file
# - Parse each character until forming a valid mul instruction
# - Each number in a mul instructions can be from 1 to 3 digits
# - Execute it, and move to next
# - Return the sum of all mul instructions responses

def process_mul(piece = ""):
    if piece.startswith("mul("):
        last_parenthesis = piece.find(")")
        comma = piece.find(",")
        fn = 0
        sn = 0
        if comma > 4 and last_parenthesis > 6 and comma < last_parenthesis:
            fn = int(piece[4:comma])
            sn = int(piece[comma + 1:last_parenthesis])
        return [fn * sn, last_parenthesis]
    return [0, 0]
    

def parse_corrupted_line(line = "", enabled = True):
    line_len = len(line)
    i = 0
    result = 0
    while i < line_len:
        if line[i] == "d":
            if line[i:i+4] == "do()":
                enabled = True
                i = i + 3
            if line[i:i+7] == "don't()":
                enabled = False
                i = i + 6
        if line[i] == "m" and enabled:
            [piece_value, valid_until] = process_mul(line[i:i+12])
            if piece_value > 0:
                result = result + piece_value
                i = i + valid_until
        i=i+1
    return [result, enabled]

def read_corrupted_memory(file_path):
    response = 0
    file=open(file_path)
    enabled = True
    for line in file:
        [result, enabled] = parse_corrupted_line(line, enabled)
        response = response + result
    return response

print(read_corrupted_memory("input.txt"))
