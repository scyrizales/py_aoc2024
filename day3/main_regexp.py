import re

def read_corrupted_memory(file_path):
    with open(file_path, 'r') as f:
        mem = f.read()
    sum_mul = 0
    
    # mem_clean = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', mem)
    # for x, y in mem_clean:
    #     sum_mul += int(x) * int(y)
    
    sum_mul = 0
    do_sum = True
    for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', mem):
        match x[0]:
            case 'do()':
                do_sum = True
            case 'don\'t()':
                do_sum = False
            case _:
                if do_sum:
                    sum_mul += int(x[1]) * int(x[2])
    return sum_mul

print(read_corrupted_memory("input.txt"))
