

string1, string2, string3 = input(), input(), input()

len1, len2, len3 = len(string1), len(string2), len(string3)

routes = [[[0] * (len3+1) for _ in range(len2+1)] for i in range(len1+1)]

answer = 0
for i in range(len1):
    for j in range(len2):
        for k in range(len3):
            if string1[i] == string2[j] and string2[j] == string3[k]:
                routes[i][j][k] = routes[i-1][j-1][k-1] + 1
            else:
                routes[i][j][k] = max(routes[i-1][j][k], routes[i][j-1][k], routes[i][j][k-1])
            answer = max(answer, routes[i][j][k])
print(answer)