x = int(input())  

count = 0

for i in range(x):
    word = list(input())
    new_word = []  

    if len(word) == 1:
        count += 1
        continue  

    is_group = True
    for j in range(len(word)):
        if j > 0 and word[j] != word[j - 1]:
            if word[j] in new_word:
                is_group = False
                break
        new_word.append(word[j])

    if is_group:
        count += 1

print(count)
