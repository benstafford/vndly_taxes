import sys
from store import Store
from scanner import Scanner

with open(sys.argv[1]) as input_file:
    data = input_file.readlines()

input_rows = [str.strip(line) for line in data]
store = Store(Scanner.scan(input_rows))
print(store.print_receipt())