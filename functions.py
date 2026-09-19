def prod_non_zero_diag(x):
    pr = 1
    for i in range(min(len(x), len(x[0]))):
        if x[i][i]:
            pr *= x[i][i]
    return pr


def are_multisets_equal(x, y):
    if len(x) != len(y):
        return False
    return sorted(x) == sorted(y)


def max_after_zero(x):
    ans = None
    for i in range (1, len(x)):
        if x[i - 1] == 0:
            if ans is None or ans < x[i]:
                ans = x[i]
    return ans


def mix_channels(img, w):
    n = len(img)
    m = len(img[0])
    c = len(w)
    ans = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0.0
            for k in range(c):
                s += img[i][j][k] * w[k]
            ans[i][j] = s
    return ans


def run_length_encoding(x):
    if len(x) == 0:
        return [], []
    v = []
    cnt = []
    pr = x[0]
    now = 1
    for z in x[1:]:
        if z == pr:
            now += 1
        else:
            v.append(pr)
            cnt.append(now)
            pr = z
            now = 1
    v.append(pr)
    cnt.append(now)
    return v, cnt


import math

def pairwise_distance(x, y):
    n = len(x)
    m = len(y)
    d = len(x[0])
    res = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0.0
            for k in range(d):
                diff = x[i][k] - y[j][k]
                s += diff * diff
            res[i][j] = math.sqrt(s)
    return res