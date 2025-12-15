import sys
from collections import deque
input = sys.stdin.readline

def FunlandandLollandSea(strArr):
    heights = []
    i = 0
    while (i < len(strArr)):
        row_s = str(strArr[i]).strip()
        parts = row_s.split(",")
        row = []
        j = 0
        while (j < len(parts)):
            row.append(int(parts[j]))
            j += 1
        heights.append(row)
        i += 1

    if (len(heights) == 0):
        return []

    m = len(heights)
    n = len(heights[0])

    canReachFunland = []
    canReachLolland = []

    i = 0
    while (i < m):
        r1 = []
        r2 = []
        j = 0
        while (j < n):
            r1.append(False)
            r2.append(False)
            j += 1
        canReachFunland.append(r1)
        canReachLolland.append(r2)
        i += 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    q = deque()
    i = 0
    while (i < m):
        q.append((i, 0))
        i += 1
    j = 0
    while (j < n):
        q.append((0, j))
        j += 1

    while (len(q) > 0):
        r, c = q.popleft()
        if (canReachFunland[r][c] == True):
            continue
        canReachFunland[r][c] = True

        t = 0
        while (t < 4):
            nr = r + dr[t]
            nc = c + dc[t]
            if (0 <= nr and nr < m and 0 <= nc and nc < n):
                if (heights[nr][nc] >= heights[r][c]):
                    q.append((nr, nc))
            t += 1

    q = deque()

    # Lolland: right + bottom
    i = 0
    while (i < m):
        q.append((i, n - 1))
        i += 1
    j = 0
    while (j < n):
        q.append((m - 1, j))
        j += 1

    while (len(q) > 0):
        r, c = q.popleft()
        if (canReachLolland[r][c] == True):
            continue
        canReachLolland[r][c] = True

        t = 0
        while (t < 4):
            nr = r + dr[t]
            nc = c + dc[t]
            if (0 <= nr and nr < m and 0 <= nc and nc < n):
                if (heights[nr][nc] >= heights[r][c]):
                    q.append((nr, nc))
            t += 1

    result = []
    i = 0
    while (i < m):
        j = 0
        while (j < n):
            if (canReachFunland[i][j] == True and canReachLolland[i][j] == True):
                result.append(str(i) + "," + str(j))
            j += 1
        i += 1

    return result


line = input()

if (type(line) == list):
    strArr = line
else:
    line = str(line).strip()
    if (line == ""):
        print([])
        sys.exit(0)

    line = line.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")

    if ((len(line) >= 2) and (line[0] == "[") and (line[len(line) - 1] == "]")):
        temp = line[1:len(line) - 1].strip()
    else:
        temp = line

    if ('","' in temp):
        raw = temp.split('","')
    elif ('", "' in temp):
        raw = temp.split('", "')
    else:
        raw = temp.split('",')

    strArr = []
    i = 0
    while (i < len(raw)):
        word = raw[i].strip()

        if (len(word) >= 1 and (word[0] == '"' or word[0] == "'")):
            word = word[1:]
        if (len(word) >= 1 and (word[len(word) - 1] == '"' or word[len(word) - 1] == "'")):
            word = word[:len(word) - 1]

        word = word.strip()
        if (word != ""):
            strArr.append(word)
        i += 1

print(FunlandandLollandSea(strArr))
