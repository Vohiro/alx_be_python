pattern  = int(input("Enter a number: "))
count = pattern

while pattern > 0:
    for pat in range(0, count):
        print("*", end="")
    print()
    pattern = pattern - 1
