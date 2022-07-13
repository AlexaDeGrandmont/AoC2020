input = []
f = open("puzzleinput.txt", "r")
for line in f:
    input.append(line.strip())

length = len(input[0])
distance = len(input)

paramList = [[1,1], [3,1], [5,1], [7,1], [1,2]]
product = 1

for param in paramList:
    width = 0
    counter = 0
    for depth in range(0, distance, param[1]):
        char = input[depth][width]
        if (char == '#'):
            counter += 1
        width = (width + param[0]) % length    
    product *= counter

print(product)