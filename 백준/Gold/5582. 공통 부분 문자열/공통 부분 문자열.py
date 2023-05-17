

string1 = input()
string2 = input()
answer = 0

routes = [[0] * (len(string2)+1) for _ in range(len(string1)+1)]

for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i] == string2[j]:
            routes[i][j] = routes[i-1][j-1] + 1
            answer = max(answer, routes[i][j])
print(answer)