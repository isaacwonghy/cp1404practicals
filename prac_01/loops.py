for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

no_of_stars = int(input("Number of stars: "))
for i in range(0, no_of_stars):
    print('*', end='')

rows = int(input("Number of stars: "))
for i in range(rows + 1):
    for j in range(i):
        print('*', end='')
    print("")
