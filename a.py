def print_a():
    a = 4
    b = 4
    result = []
    for y in range(a):
        result.append([])
        for x in range(b):
            result[y].append(0)
    # start = [0][0]
    current_x = 0
    current_y = 0
    i = 1
    j = 0
    count = 1
    max_x = 3
    max_y = 3
    min_x = 0
    min_y = 0
    for y in range(a):
        for x in range(b):
            print("round:",int(y/2) % 2)
            print("cur", current_y, current_x)
            result[current_y][current_x] = count
            # print(max_x)
            if (current_x == max_x and i == 1) or (current_x == 0 and i == -1):
                
                i = 0
                if int(y/2) % 2 == 0:
                    j = 1
                else:
                    j = -1
                    max_x = max_x - 1
                    print(max_x)
                    # min_x = min_x +1
            elif ((current_y == max_y and j == 1) or (current_y == 0 and j == -1)):
                max_y = max_y - 1
                j = 0
                # print(int(y/2))
                # print(int(y/2) % 2)
                if int(y/2) % 2 == 0:
                    i = -1
                else:
                    i = 1
            current_y = current_y+j
            current_x = current_x+i
            count +=1
    # print(result)

    for y in range(a):
        for x in range(b):
            print(result[y][x], end =" ")
        print("\n", end="")

# max = 16
            

print_a()

# 1  2  3  4
# 12 13 14 5
# 11 16 15  6
# 10  9  8  7