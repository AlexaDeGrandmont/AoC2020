f = open("puzzleinput.txt", "r")
input = f.read().split('\n\n')

forms = []

for i in input:
    forms.append(i.replace('\n', ' ').split())

chars = []
counter = 0
total = 0

for form in forms:
    for entry in form:
        for char in entry:
            if char not in chars:
                chars.append(char)   
                counter += 1 
    chars = []
    total += counter
    counter = 0

print(total)