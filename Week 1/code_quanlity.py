def calc(a, b, c=[]):  # function definition block
    x = 0  # initialisation block
    for i in a:  # loop block
        if (i > 10):
            x = x + i
        else:
            x = x - 1  # conditional decision block inside loop
    if b == True: print("Result is:", x)  # conditional output block
    return x  # return block


data = [1, 5, 12, 20, 3]
result = calc(data, True)  # function call block
print(result)  # output block
