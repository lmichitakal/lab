def n_gram(n, S):
    return [S[idx:idx + n] for idx in range(len(S) - n + 1)]
S1 = 'paraparaparadise'
S2 = 'paragraph'
X = n_gram(2, S1)
Y = n_gram(2, S2)
print("和集合：{}\n積集合：{}\n差集合：{}".format(set(X) | set(Y), set(X) & set(Y), set(X) - set(Y)))
print('se' in (set(X) & set(Y)))