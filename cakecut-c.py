from scipy.optimize import linprog

def backtrack(n, t, mat1, mat2, chosen1, chosen2, b, cnt1, cnt2, count1, count2):
    if t == 2 * n:
        if cnt1 < count1 or cnt2 < count2:
            return 0, [], []
        Ae = [[0 for _ in range(count1 + count2 + 1)] for _ in range(count1 + count2)]
        Be = [0 for _ in range(count1 + count2)]
        A = [[0 for _ in range(count1 + count2 + 1)] for _ in range(2 * n)]
        B = [0 for _ in range(2 * n)]
        C = [0 for _ in range(count1 + count2 + 1)]
        C[count1 + count2] = 1
        Ae[0] = [1 for _ in range(count2)] + [0 for _ in range(count1 + 1)]
        Ae[1] = [0 for _ in range(count2)] + [1 for _ in range(count1)] + [0]
        Be[0] = 1
        Be[1] = 1
        for j in range(1, count1):
            for k in range(count2):
                Ae[j + 1][k] = mat1[chosen1[j]][chosen2[k]] - mat1[chosen1[j - 1]][chosen2[k]]
        for j in range(1, count2):
            for k in range(count1):
                Ae[j + count1][k + count2] = mat2[chosen1[k]][chosen2[j]] - mat2[chosen1[k]][chosen2[j - 1]]
        ptr = 0
        for j in range(n):
            if b[j] == 0:
                for k in range(count2):
                    A[ptr][k] = mat1[j][chosen2[k]] - mat1[chosen1[0]][chosen2[k]]
                ptr += 1
        for j in range(n, 2 * n):
            if b[j] == 0:
                for k in range(count1):
                    A[ptr][k + count2] = mat2[chosen1[k]][j - n] - mat2[chosen1[k]][chosen2[0]]
                ptr += 1
        for j in range(count2):
            A[j + 2 * n - count1 - count2][j] = -1
            A[j + 2 * n - count1 - count2][count1 + count2] = 1
        for j in range(count1):
            A[j + 2 * n - count1][j + count2] = -1
            A[j + 2 * n - count1][count1 + count2] = 1
        f = linprog(c=C, A_ub=A, b_ub=B, A_eq=Ae, b_eq=Be, method='simplex')
        if f.success:
            return 1, b, f.x
        return 0, [0 for _ in range(2*n)], []
    if count1 > cnt1 and t < n:
        b[t] = 1
        [res, bp, P] = backtrack(n, t + 1, mat1, mat2, chosen1 + [t], chosen2, b, cnt1 + 1, cnt2, count1, count2)
        if res == 1:
            return res, bp, P
    if count2 > cnt2 and t >= n:
        if count1 > cnt1:
            return 0, [0 for _ in range(2*n)], []
        b[t] = 1
        [res, bp, P] = backtrack(n, t + 1, mat1, mat2, chosen1, chosen2 + [t - n], b, cnt1, cnt2 + 1, count1, count2)
        if res == 1:
            return res, bp, P
    b[t] = 0
    return backtrack(n, t + 1, mat1, mat2, chosen1, chosen2, b, cnt1, cnt2, count1, count2)


def main(n, mat1, mat2):
    maxs1 = [[0 for _ in range(n)] for _ in range(n)]
    maxs2 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        ptrmax1, ptrmax2 = 0, 0
        for j in range(n):
            if mat2[i][j] > mat2[i][ptrmax2]:
                ptrmax2 = j
            if mat1[j][i] > mat1[ptrmax1][i]:
                ptrmax1 = j
        for j in range(n):
            if mat2[i][j] == mat2[i][ptrmax2]:
                maxs2[i][j] += 1
            if mat1[j][i] == mat1[ptrmax1][i]:
                maxs1[j][i] += 1
    cnt = 0
    xs = []
    ys = []
    ans = []
    for i in range(n):
        for j in range(n):
            if maxs1[i][j] >= 1 and maxs2[i][j] >= 1:
                cnt += 1
                xs += [i + 1]
                ys += [j + 1]
    ans += [cnt]
    tmpans = []
    for i in range(len(xs)):
        tmpans += [(xs[i], ys[i])]
    ans += [tmpans]
    for i in range(3, 2 * n):
        for j in range(max(1,i-n+1), min(2*n-i, i)):
            A, b, B = backtrack(n, 0, mat1, mat2, [], [], [0 for _ in range(2 * n)], 0, 0, j, i - j)
            if A == 1:
                sum = 0
                for ik in range(i):
                    if B[ik] > 0:
                        sum += 1
                if sum == i:
                    t = 1
                    a = []
                    ptr = 0
                    if t > 0:
                        for m in range(n):
                            if b[m] == 1:
                                a += [B[ptr + i - j]]
                                ptr += 1
                            else:
                                a += [0.0]
                        ans += [a]
                        a = []
                        ptr = 0
                        for m in range(n):
                            if b[m + n] == 1:
                                a += [B[ptr]]
                                ptr += 1
                            else:
                                a += [0.0]
                        ans += [a]
                        i = 2 * n
                    break
    return ans
#print(main(3, [[1, 2, 2], [3, 1, 3], [2, 2, 8]], [[1, 3, 5], [6, 8, 5], [7, 10, 5]]))