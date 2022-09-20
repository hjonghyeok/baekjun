from re import S


a = input()
s = 0
for i in a:
    if i == 'A' or i == 'B' or i == 'C':
        s += 3
    elif i == 'D' or i == 'E' or i == 'F':
        s += 4
    elif i == 'G' or i == 'H' or i == 'I':
        s += 5
    elif i == 'J' or i == 'K' or i == 'L':
        s += 6
    elif i == 'M' or i == 'N' or i == 'O':
        s += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        s += 8
    elif i == 'T' or i == 'U' or i == 'V':
        s += 9 
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        s += 10
print(s)