input = []
f = open("puzzleinput.txt", "r")
for line in f:
    input.append(line.strip())

length = len(input[0])
distance = len(input)

width = 0
char = input[0][width]
counter = 0

for depth in range(1, distance):
    width = (width + 3) % length
    char = input[depth][width]
    if (char == '#'):
        counter += 1

print(counter)
    