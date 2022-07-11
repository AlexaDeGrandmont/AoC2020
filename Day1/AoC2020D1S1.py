input = []
f = open("puzzleinput.txt", "r")
for line in f:
    input.append(line.strip())

for first in input:
    for second in input:
        if (first != second):
            if (int(first) + int(second) == 2020):
                print(int(first) * int(second))
        

