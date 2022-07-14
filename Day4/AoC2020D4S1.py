f = open("puzzleinput.txt", "r")
input = f.read().split('\n\n')

passports = []

for i in input:
    passports.append(i.replace('\n', ' ').split())

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
numValid = 0

for passport in passports:
    counter = 0
    for f in fields:
        for p in passport:
            if p.split(':')[0] == f:
                counter += 1
    if counter == len(fields):
        numValid += 1

print(numValid)

