T = int(input())

getindex = lambda x : ord(x) - ord('A')
d = {}
strings = []
for _ in range(T):
    string = input()[::-1]
    for ind in range(len(string)):
        alpha = string[ind]
        if alpha not in d:
            d[alpha] = 10**ind
        else:
            d[alpha] += 10**ind
    strings.append(string[::-1])

num = 9
orders = [(val, key) for key, val in d.items()]
orders.sort(reverse=True)
alp_to_num = {}
for val, key in orders:
    alp_to_num[key] = num
    num -= 1

answer = 0
for string in strings:
    num = ''.join(tuple(map(lambda x : str(alp_to_num[x]), string)))
    answer += int(num)

print(answer)