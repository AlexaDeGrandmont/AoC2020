input = []
f = open("puzzleinput.txt", "r")
for line in f:
    input.append(line.strip())

for first in input:
    for second in input:
        for third in input:
            if ((first != second) and (second != third) and (first != third)):
                if (int(first) + int(second) + int(third) == 2020):
                    print(int(first) * int(second) * int(third))
        

