import sys
from collections import deque
input = sys.stdin.readline

def coco_language(words):
    latter = {}
    i = 0
    while (i < len(words)):
        word = words[i]
        j = 0
        while (j < len(word)):
            count = word[j]
            if (count not in latter):
                latter[count] = 0
            j += 1
        i += 1

    x = {}
    y = {}
    for count in latter:
        x[count] = []
        y[count] = 0

    i = 0
    while (i < len(words) - 1):
        a = words[i]
        b = words[i + 1]

        j = 0
        different = False
        while (j < len(a) and j < len(b)):
            if (a[j] != b[j]):
                u = a[j]
                v = b[j]

                exist = False
                k = 0
                while (k < len(x[u])):
                    if (x[u][k] == v):
                        exist = True
                        break
                    k += 1

                if (exist == False):
                    x[u].append(v)
                    y[v] += 1

                different = True
                break
            j += 1

        if ((different == False) and (len(a) > len(b))):
            return ""

        i += 1

    use = {}
    for count in latter:
        use[count] = False

    q = deque()
    for count in y:
        if (y[count] == 0):
            q.append(count)

    ans = []
    clear = 0
    all = 0
    for _ in latter:
        all += 1

    while (len(q) > 0):
        select = q.popleft()
        if (use[select] == True):
            continue

        use[select] = True
        ans.append(select)
        clear += 1

        k = 0
        while (k < len(x[select])):
            nxt = x[select][k]
            y[nxt] -= 1
            if (y[nxt] == 0):
                q.append(nxt)
            k += 1

    if (clear != all):
        return ""

    return "".join(ans)


line = input()
# 어떤 환경에서는 line이 이미 list로 들어올 수 있어서 분기 처리
if (type(line) == list):
    words = line
else:
    line = str(line).strip()
    if (line == ""):
        print("")
        sys.exit(0)

    if (line[0] == "["):
        temp = line[1:len(line) - 1]
        raw = temp.split(",")
    else:
        raw = line.split(",")

    words = []
    i = 0
    while (i < len(raw)):
        word = raw[i].strip()

        if (len(word) >= 2):
            if (((word[0] == '"') and (word[len(word) - 1] == '"')) or ((word[0] == "'") and (word[len(word) - 1] == "'"))):
                word = word[1:len(word) - 1]

        if (word != ""):
            words.append(word)
        i += 1

print(coco_language(words))
