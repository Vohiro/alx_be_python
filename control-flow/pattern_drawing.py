pattern  = int(input("Enter the size of the pattern: "))
count = pattern

while pattern > 0:
    for pat in range(0, count):
        print("*", end="")
    print()
    pattern = pattern - 1
