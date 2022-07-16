f = open("puzzleinput.txt", "r")
input = f.read().split('\n\n')

forms = []

for i in input:
    forms.append(i.replace('\n', ' ').split())

chars = []
counter = 0
total = 0

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for form in forms:
    for letter in alphabet:
        for entry in form:
            if letter in entry:
                counter += 1
        if counter == len(form):
            total += 1
        counter = 0

print(total)
        
