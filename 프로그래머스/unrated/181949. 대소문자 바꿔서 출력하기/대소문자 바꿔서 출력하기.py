str = input()
string = [string.lower() if string.upper() == string else string.upper() for string in str]
print(''.join(string))