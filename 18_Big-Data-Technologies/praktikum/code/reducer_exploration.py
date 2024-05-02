import sys

for line in sys.stdin:
    key, value = line.strip().split("\t\t")
    
    print(f"{key}\t\t{value}")