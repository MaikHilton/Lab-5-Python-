size = 7
array = [[1 for k in range(size)] for k in range(size)]

for i in range(size):
    if i <= 3:
        for j in range(i + 1):
            array[i][j] = 0
    else:
        for j in range(7 - i):
            array[i][j] = 0

for row in array:
    print(' '.join(map(str, row)))
