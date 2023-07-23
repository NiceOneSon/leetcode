word = input()

word_len = len(word)

left, right = 0, word_len - 1

while left < right and word[left] == word[right]:
    left += 1
    right -= 1

if not left < right:
    print(1)
else:
    print(0)