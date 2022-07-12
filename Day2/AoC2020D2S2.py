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
    if (password[3][int(password[0]) -1] == password[2]) or (password[3][int(password[1]) -1] == password[2]):
        if (password[3][int(password[0]) -1] == password[2]) and (password[3][int(password[1]) -1] == password[2]):
            counter += 0
        else:
            counter += 1

print(counter)