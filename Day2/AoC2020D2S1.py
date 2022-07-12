input = []
f = open("puzzleinput.txt", "r")
for line in f:
    input.append(line.strip())

passwords = []

for line in input:
    line = line.replace(':','')
    passwords.append(line.replace('-', ' ').split())

counter = 0

for password in passwords:
    numChar = password[3].count(password[2])
    if ((numChar >= int(password[0])) and (numChar <= int(password[1]))):
        counter += 1

print(counter)
