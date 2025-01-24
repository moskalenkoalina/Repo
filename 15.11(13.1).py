def readfile(filename):
    with open(filename,encoding="utf-8") as f:
        lines = f.readlines()
        return lines

def print_long(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if len(line.strip()) > 60:
                print(line.strip())

def count(filename):
    a = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if  not line.strip():
                a += 1
    return a

def longest(filename):
    longest_line = ""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in file:
            if len(line) > len(longest_line):
                longest_line = line
            return longest_line.strip()
