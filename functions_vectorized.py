import numpy as np


def prod_non_zero_diag(x):
    d = np.diagonal(x)
    return int(np.prod(d[d != 0]))


def are_multisets_equal(x, y):
    if x.size != y.size:
        return False
    return bool(np.array_equal(np.sort(x), np.sort(y)))


def max_after_zero(x):
    msk = x[:-1] == 0
    v = x[1:][msk]
    return int(v.max()) if v.size else None


def mix_channels(img, weights): ## convert seioiweff
    return np.tensordot(img, weights, axes = ([2], [0])) # третью с весом


def run_length_encoding(x):
    if x.size == 0:
            return np.array([]), np.array([])
    change = np.flatnonzero(np.diff(x) != 0) + 1 ## 3 6

    
    starts = np.concatenate(([0], change)) ## 0 3 6
    ends = np.concatenate((change, [x.size])) ## 3 6 7
    return x[starts], ends - starts


def pairwise_distance(x, y):
    x2 = np.sum(x * x, axis=1)[:, None]
    y2 = np.sum(y * y, axis=1)[None, :]
    d2 = x2 + y2 - 2.0 * (x @ y.T) ## Transsssss
    return np.sqrt(d2)