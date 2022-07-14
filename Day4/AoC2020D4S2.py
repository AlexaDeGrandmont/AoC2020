f = open("puzzleinput.txt", "r")
input = f.read().split('\n\n')

passports = []

for i in input:
    passports.append(i.replace('\n', ' ').split())

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
numPresent = 0
presentPassports = []

for passport in passports:
    counter = 0
    for f in fields:
        for p in passport:
            if p.split(':')[0] == f:
                counter += 1
    if counter == len(fields):
        numPresent += 1
        presentPassports.append(passport);

def checkBirthYear(byr):
    if len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002:
        return True
    return False    

def checkIssueYear(iyr):
    if len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020:
        return True
    return False

def checkExpYear(eyr):
    if len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030:
        return True
    return False

def checkHeight(hgt):
    if hgt[-2:] == 'cm' and int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193:
        return True
    elif hgt[-2:] == 'in' and int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76:
        return True
    else:
        return False

def checkHairColour(hcl):
    hexchars = '0123456789abcdef'
    if hcl[0] == '#':
        if all(char in hexchars for char in hcl[1:]):
            return True
    return False

def checkEyeColour(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def checkPassportID(pid):
    if len(pid) == 9 and pid.isnumeric():
        return True
    return False

numValid = 0

for pp in presentPassports:
    counter = 0
    for field in pp:
        if field.split(':')[0] == 'byr':
            if checkBirthYear(field.split(':')[1]):
                counter += 1
        elif field.split(':')[0] == 'iyr':
            if checkIssueYear(field.split(':')[1]):
                counter += 1
        elif field.split(':')[0] == 'eyr':
            if checkExpYear(field.split(':')[1]):
                counter += 1
        elif field.split(':')[0] == 'hgt':
            if checkHeight(field.split(':')[1]):
                counter += 1
        elif field.split(':')[0] == 'hcl':
            if checkHairColour(field.split(':')[1]):
                counter += 1
        elif field.split(':')[0] == 'ecl':
            if checkEyeColour(field.split(':')[1]):
                counter += 1
        elif field.split(':')[0] == 'pid':
            if checkPassportID(field.split(':')[1]):
                counter += 1
    if counter == len(fields):
        numValid += 1

print(numValid)


  

