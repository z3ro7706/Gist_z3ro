def CoCoLanguage(strArr):
    arr = strArr
    n = len(arr)

    if (n == 0):
        return ""

    g = {}
    indeg = {}
    i = 0
    while (i < n):
        word = arr[i]
        j = 0
        while (j < len(word)):
            ch = word[j]
            if (ch not in g):
                g[ch] = []
                indeg[ch] = 0
            j += 1
        i += 1

    i = 0
    while (i < n - 1):
        w1 = arr[i]
        w2 = arr[i + 1]
        len1 = len(w1)
        len2 = len(w2)
        j = 0
        while (j < len1 and j < len2 and w1[j] == w2[j]):
            j += 1
        if (j == len2 and len1 > len2):
            return ""
        if (j < len1 and j < len2):
            u = w1[j]
            v = w2[j]
            exist = False
            k = 0
            while (k < len(g[u])):
                if (g[u][k] == v):
                    exist = True
                    break
                k += 1
            if (not exist):
                g[u].append(v)
                indeg[v] += 1
        i += 1

    q = []
    for ch in g:
        if (indeg[ch] == 0):
            q.append(ch)
    ans = []
    while (q):
        u = q.pop(0)
        ans.append(u)
        k = 0
        while (k < len(g[u])):
            v = g[u][k]
            indeg[v] -= 1
            if (indeg[v] == 0):
                q.append(v)
            k += 1
    if (len(ans) != len(g)):
        return ""

    return ""

x=list(input())
print(CoCoLanguage(x))
