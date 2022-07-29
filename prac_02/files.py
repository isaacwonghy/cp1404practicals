OUTPUT_FILE = 'name.txt'

# 1
out_file = open(OUTPUT_FILE, 'w')
name = input("What's your name?")
print(name, file=out_file)
out_file.close()

# 2
in_file = open(OUTPUT_FILE, 'r')
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# 3
filename = 'numbers.txt'

in_file = open(filename, "r")
first_line = in_file.readline()
second_line = in_file.readline()
total = int(first_line) + int(second_line)
print(total)
in_file.close()

# 4
in_file = open(filename, 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
