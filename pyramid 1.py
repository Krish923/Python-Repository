def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        a=i
        print(" "*(rows-i), end="")
        for j in range(2 * a - 1):
            print(j + 1, end="")
        print()
r=int(input())
print_number_pyramid(r)