import sys

def is_palindrome(word):
    return word == word[::-1]

for line in sys.stdin:
    value = line.strip()
    
    if is_palindrome(value):
        print(f"{value}\t\tTrue")
    else:
        print(f"{value}\t\tFalse")