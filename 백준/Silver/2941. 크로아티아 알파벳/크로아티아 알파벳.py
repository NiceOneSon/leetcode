croatia = 'c=, c-, dz=, d-, lj, nj, s=, z='
croatia = croatia.split(', ')
croatia = set(croatia)
string = input()
answer = 0
while string:
    if len(string) >= 3 and string[:3] == 'dz=':
        string = string[3:]
        answer += 1
    elif len(string) >= 2 and string[:2] in croatia:
        string = string[2:]
        answer += 1
    else:
        string = string[1:]
        answer += 1
print(answer)