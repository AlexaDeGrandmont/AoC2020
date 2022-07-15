input = []
f = open("puzzleinput.txt", "r")
for line in f:
    input.append(line.strip())

def binarySearch(start, end, boardingPass, index, indexStop):
    while index < indexStop:
        if boardingPass[index] == 'F' or boardingPass[index] == 'L':
            end = (start + end) // 2
            return binarySearch(start, end, boardingPass, index+1, indexStop)  
        elif boardingPass[index] == 'B' or boardingPass[index] == 'R':
            start = (start + end) // 2 + 1
            return binarySearch(start, end, boardingPass, index+1, indexStop)  
    if start == end:
        return start

seatIDs = []

for boardingPass in input:
    row = binarySearch(0, 127, boardingPass, 0, 7)
    column = binarySearch(0, 7, boardingPass, 7, 10)
    seatIDs.append((row * 8) + column)

max = 0
for seatID in seatIDs:
    if seatID > max:
        max = seatID

seatIDs.sort()

for x in range(0, len(seatIDs) - 1):
    if seatIDs[x+1] - seatIDs[x] == 2:
        print(seatIDs[x]+1)
    


