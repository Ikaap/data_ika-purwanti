import sys

line_number = 1

for line in sys.stdin:
    number = line.strip()
    
    print(f"{line_number}. {number}")
    line_number += 1