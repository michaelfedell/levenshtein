import sys

if len(sys.argv) != 3:
    raise TypeError('Function requries exactly two arguments. You supplied {}'.format(len(sys.argv) - 1))

w1, w2 = sys.argv[1].lower(), sys.argv[2].lower()

def lev(word1, word2):
    m, n = len(word1) + 1, len(word2) + 1
    v = [None] * (n)
    for i in range(n):
        v[i] = [None] * (m)
    v[0] = list(range(m))
    for i in range(n):
        v[i][0] = i

    for i in range(1, n):
        for j in range(1, m):
            v[i][j] = min(
                v[i-1][j] + 1,
                v[i][j-1] + 1,
                v[i-1][j-1] + 2 * (1 if word1[j-1]!=word2[i-1] else 0)
            )

    for i in v:
        print(i)

    return v[n-1][m-1]

print(lev(w1, w2))
