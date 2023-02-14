string1 = input()
string2 = input()

if len(string1) > len(string2):
    string1, string2 = string2, string1
routes = [[0] * (len(string2)) for i in range(len(string1))]

for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i] == string2[j]:
            if i and j:
                routes[i][j] = routes[i-1][j-1] + 1
            else:
                routes[i][j] = 1
        else:
            if i and j:
                routes[i][j] = max(routes[i-1][j-1], routes[i-1][j], routes[i][j-1])
            else:
                routes[i][j] = max(routes[max(0, i-1)][j], routes[i][max(0, j-1)])
print(routes[-1][-1])