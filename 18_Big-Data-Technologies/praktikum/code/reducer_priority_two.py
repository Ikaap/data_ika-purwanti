import sys

total = 0
count = 0

for line in sys.stdin:
    key, value = line.split(".")
    
    total += float(value)
    count += 1
    
    
average = total / count    
print("Average: ", str(average))