def n_gram(n, S):
    return [S[idx:idx + n] for idx in range(len(S) - n + 1)]

S1 = 'paraparaparadise'
S2 = 'paragraph'
X = n_gram(2, S1)
Y = n_gram(2, S2)

union = set(X) | set(Y)
intersection = set(X) & set(Y)
diff = set(X) - set(Y)

print("和集合：{}\n積集合：{}\n差集合：{}".format(union, intersection, diff))
print('se' in (intersection))