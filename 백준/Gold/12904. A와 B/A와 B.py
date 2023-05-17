string1 = input()
string2 = input()
left, right = string1[0], string1[-1]

while string2 and len(string2) > len(string1):
    if string2[-1] == 'A':
        string2 = string2[:-1]
    elif string2[-1] == 'B':
        string2 = string2[:-1][::-1]
    
    
if string2 == string1:
    print(1)
else:
    print(0)