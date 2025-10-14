word = list(input())
i = 0
count = 0

while i < len(word):
    if word[i] == "c":
        if i + 1 < len(word) and (word[i+1] == "=" or word[i+1] == "-"):
            i += 2
        else:
            i += 1
        count += 1

    elif word[i] == "d":
        if i + 2 < len(word) and word[i+1] == "z" and word[i+2] == "=":
            i += 3
        elif i + 1 < len(word) and word[i+1] == "-":
            i += 2
        else:
            i += 1
        count += 1

    elif word[i] == "l":
        if i + 1 < len(word) and word[i+1] == "j":
            i += 2
        else:
            i += 1
        count += 1

    elif word[i] == "n":
        if i + 1 < len(word) and word[i+1] == "j":
            i += 2
        else:
            i += 1
        count += 1

    elif word[i] == "s":
        if i + 1 < len(word) and word[i+1] == "=":
            i += 2
        else:
            i += 1
        count += 1

    elif word[i] == "z":
        if i + 1 < len(word) and word[i+1] == "=":
            i += 2
        else:
            i += 1
        count += 1

    else:
        i += 1
        count += 1

print(count)
