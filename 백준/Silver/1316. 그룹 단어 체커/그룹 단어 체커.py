N = int(input())
answer = 0
for i in range(N):
    word = input()
    prev = word[0]
    s = set(prev)
    for j in range(1, len(word)):
        string = word[j]
        if prev != string and string in s:
            break
        prev = string
        s.add(string)
    else:
        answer += 1
print(answer)