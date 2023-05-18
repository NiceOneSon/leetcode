string1 = input()
string2 = input()

routes = [[0] * (len(string2)+1) for _ in range(len(string1)+1)]

for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i] == string2[j]:
            routes[i][j] += routes[i-1][j-1] + 1
        else:
            routes[i][j] = max(routes[i-1][j], routes[i][j-1], routes[i-1][j-1])
print(routes[len(string1)-1][len(string2)-1])
