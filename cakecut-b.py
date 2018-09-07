def Eval(x, y, segment, index, total):
    summ = 0
    for i in range(len(segment[index])):
        if x <= segment[index][i][0] < segment[index][i][1] <= y:
            summ += segment[index][i][1] - segment[index][i][0]
        elif x <= segment[index][i][0] < y < segment[index][i][1]:
            summ += y - segment[index][i][0]
        elif segment[index][i][0] < x < segment[index][i][1] <= y:
            summ += segment[index][i][1] - x
    return summ / total


def Cut(x, val, segment, index, total):
    summ = 0
    for i in range(len(segment[index])):
        if x <= segment[index][i][0]:
            if summ + (segment[index][i][1] - segment[index][i][0]) > val * total:
                return val * total - summ + segment[index][i][0]
            summ += segment[index][i][1] - segment[index][i][0]
        elif segment[index][i][0] < x < segment[index][i][1]:
            if summ + segment[index][i][1] - x > val * total:
                return val * total - summ + x
            summ += segment[index][i][1] - x
    return 100


def Three(segments_list, total, i, j, k, tah):
    flag = 0
    value = tah / 2
    dif = tah / 4
    while flag == 0:
        y1 = Cut(value, (Eval(0, tah, segments_list, i, total[i]) - Eval(0, value, segments_list, i, total[i])) / 2,
                 segments_list, i, total[i])
        y2 = Cut(value, (Eval(0, tah, segments_list, j, total[j]) - Eval(0, value, segments_list, j, total[j])) / 2,
                 segments_list, j, total[j])
        y3 = Cut(value, (Eval(0, tah, segments_list, k, total[k]) - Eval(0, value, segments_list, k, total[k])) / 2,
                 segments_list, k, total[k])
        # print(y1, y2, y3)
        ymid = y1
        if y1 < y2 < y3 or y1 > y2 > y3:
            ymid = y2
        elif y2 < y3 < y1 or y2 > y3 > y1:
            ymid = y3
        v11 = Eval(0, value, segments_list, i, total[i])
        v21 = Eval(0, value, segments_list, j, total[j])
        v31 = Eval(0, value, segments_list, k, total[k])
        v12 = Eval(value, ymid, segments_list, i, total[i])
        v22 = Eval(value, ymid, segments_list, j, total[j])
        v32 = Eval(value, ymid, segments_list, k, total[k])
        v13 = Eval(ymid, tah, segments_list, i, total[i])
        v23 = Eval(ymid, tah, segments_list, j, total[j])
        v33 = Eval(ymid, tah, segments_list, k, total[k])
        t1 = ""
        t2 = ""
        t3 = ""
        # print(ymid, value)
        if v11 - v12 >= -1e-7 and v11 - v13 >= -1e-7:
            t1 += "1"
        if v12 - v11 >= -1e-7 and v12 - v13 >= -1e-7:
            t1 += "2"
        if v13 - v12 >= -1e-7 and v13 - v11 >= -1e-7:
            t1 += "3"
        if v21 - v22 >= -1e-7 and v21 - v23 >= -1e-7:
            t2 += "1"
        if v22 - v21 >= -1e-7 and v22 - v23 >= -1e-7:
            t2 += "2"
        if v23 - v22 >= -1e-7 and v23 - v21 >= -1e-7:
            t2 += "3"
        if v31 - v32 >= -1e-7 and v31 - v33 >= -1e-7:
            t3 += "1"
        if v32 - v31 >= -1e-7 and v32 - v33 >= -1e-7:
            t3 += "2"
        if v33 - v32 >= -1e-7 and v33 - v31 >= -1e-7:
            t3 += "3"
        #print(t1, t2, t3)
        #print(value, ymid)
        if (t1 == "1" and (t2 == "1" or t3 == "1")) or (t2 == "1" and t3 == "1"):
            value = value - dif
            dif = dif / 2
        elif '1' not in t1 and '1' not in t2 and '1' not in t3:
            value = value + dif
            dif = dif / 2
        else:
            i += 1
            j += 1
            k += 1
            if '1' in t1 and '2' in t2 and '3' in t3:
                return [round(value, 6), round(ymid, 6)], [i, j, k]
            if '1' in t1 and '2' in t3 and '3' in t2:
                return [round(value, 6), round(ymid, 6)], [i, k, j]
            if '1' in t2 and '2' in t1 and '3' in t3:
                return [round(value, 6), round(ymid, 6)], [j, i, k]
            if '1' in t2 and '2' in t3 and '3' in t1:
                return [round(value, 6), round(ymid, 6)], [j, k, i]
            if '1' in t3 and '2' in t2 and '3' in t1:
                return [round(value, 6), round(ymid, 6)], [k, j, i]
            if '1' in t3 and '2' in t1 and '3' in t2:
                return [round(value, 6), round(ymid, 6)], [k, i, j]
            if '1' in t1:
                return [round(value, 6), round(ymid, 6)], [i, j, k]
            if '1' in t2:
                return [round(value, 6), round(ymid, 6)], [j, i, k]
            if '1' in t3:
                return [round(value, 6), round(ymid, 6)], [k, j, i]
            i -= 1
            j -= 1
            k -= 1

def main(n, segments_list):
    total = [0 for _ in range(n)]
    for index in range(n):
        for i in range(len(segments_list[index])):
            total[index] += (segments_list[index][i][1] - segments_list[index][i][0])
    if n == 2:
        y = Cut(0, 0.5, segments_list, 0, total[0])
        t = Eval(0, y, segments_list, 1, total[1])
        if t >= 0.5:
            return [y], [2, 1]
        else:
            return [y], [1, 2]
    if n == 3:
        return Three(segments_list, total, 0, 1, 2, 100)
    else:
        value = 70
        dif = 27
        flag = 0
        while flag == 0:
            flags4 = 0
            flagg4 = 0
            # print("resid")
            [val, ymid], [i, j, k] = Three(segments_list, total, 0, 1, 2, value)
            # print(ymid, val, i, j, k)
            i = i - 1
            j = j - 1
            k = k - 1
            tmptmp = Eval(value, 100, segments_list, 3, total[3])
            if Eval(0, val, segments_list, 3, total[3]) - tmptmp >= 1e-7:
                flags4 += 1
            if Eval(val, ymid, segments_list, 3, total[3]) - tmptmp >= 1e-7:
                flags4 += 1
            if Eval(ymid, value, segments_list, 3, total[3]) - tmptmp >= 1e-7:
                flags4 += 1
            if Eval(value, 100, segments_list, i, total[i]) - Eval(0, val, segments_list, i, total[i]) >= 1e-7:
                flagg4 += 1
            if Eval(value, 100, segments_list, j, total[j]) - Eval(val, ymid, segments_list, j, total[j]) >= 1e-7:
                flagg4 += 1
            if Eval(value, 100, segments_list, k, total[k]) - Eval(ymid, value, segments_list, k, total[k]) >= 1e-7:
                flagg4 += 1
            if flagg4 == 0 and flags4 == 0:
                return [round(val, 5), round(ymid, 5), round(value, 5)], [i + 1, j + 1, k + 1, 4]
            flags3 = 0
            flagg3 = 0
            # print("resid")
            [val, ymid], [i, j, k] = Three(segments_list, total, 0, 1, 3, value)
            # print(ymid, val, i, j, k)
            i = i - 1
            j = j - 1
            k = k - 1
            tmptmp = Eval(value, 100, segments_list, 2, total[2])
            if Eval(0, val, segments_list, 2, total[2]) - tmptmp >= 1e-7:
                flags3 += 1
            if Eval(val, ymid, segments_list, 2, total[2]) - tmptmp >= 1e-7:
                flags3 += 1
            if Eval(ymid, value, segments_list, 2, total[2]) - tmptmp >= 1e-7:
                flags3 += 1
            if Eval(value, 100, segments_list, i, total[i]) - Eval(0, val, segments_list, i, total[i]) >= 1e-7:
                flagg3 += 1
            if Eval(value, 100, segments_list, j, total[j]) - Eval(val, ymid, segments_list, j, total[j]) >= 1e-7:
                flagg3 += 1
            if Eval(value, 100, segments_list, k, total[k]) - Eval(ymid, value, segments_list, k, total[k]) >= 1e-7:
                flagg3 += 1
            if flagg3 == 0 and flags3 == 0:
                return [round(val, 5), round(ymid, 5), round(value, 5)], [i + 1, j + 1, k + 1, 3]
            flags2 = 0
            flagg2 = 0
            # print("resid")
            [val, ymid], [i, j, k] = Three(segments_list, total, 0, 3, 2, value)
            # print(ymid, val, i, j, k)
            i = i - 1
            j = j - 1
            k = k - 1
            tmptmp = Eval(value, 100, segments_list, 1, total[1])
            if Eval(0, val, segments_list, 1, total[1]) - tmptmp >= 1e-7:
                flags2 += 1
            if Eval(val, ymid, segments_list, 1, total[1]) - tmptmp >= 1e-7:
                flags2 += 1
            if Eval(ymid, value, segments_list, 1, total[1]) - tmptmp >= 1e-7:
                flags2 += 1
            if Eval(value, 100, segments_list, i, total[i]) - Eval(0, val, segments_list, i, total[i]) >= 1e-7:
                flagg2 += 1
            if Eval(value, 100, segments_list, j, total[j]) - Eval(val, ymid, segments_list, j, total[j]) >= 1e-7:
                flagg2 += 1
            if Eval(value, 100, segments_list, k, total[k]) - Eval(ymid, value, segments_list, k, total[k]) >= 1e-7:
                flagg2 += 1
            if flagg2 == 0 and flags2 == 0:
                return [round(val, 5), round(ymid, 5), round(value, 5)], [i + 1, j + 1, k + 1, 2]
            flags1 = 0
            flagg1 = 0
            [val, ymid], [i, j, k] = Three(segments_list, total, 3, 1, 2, value)
            # print(ymid, val, i, j, k)
            i = i - 1
            j = j - 1
            k = k - 1
            tmptmp = Eval(value, 100, segments_list, 0, total[0])
            if Eval(0, val, segments_list, 0, total[0]) - tmptmp >= 1e-7:
                flags1 += 1
            if Eval(val, ymid, segments_list, 0, total[0]) - tmptmp >= 1e-7:
                flags1 += 1
            if Eval(ymid, value, segments_list, 0, total[0]) - tmptmp >= 1e-7:
                flags1 += 1
            if Eval(value, 100, segments_list, i, total[i]) - Eval(0, val, segments_list, i, total[i]) >= 1e-7:
                flagg1 += 1
            if Eval(value, 100, segments_list, j, total[j]) - Eval(val, ymid, segments_list, j, total[j]) >= 1e-7:
                flagg1 += 1
            if Eval(value, 100, segments_list, k, total[k]) - Eval(ymid, value, segments_list, k, total[k]) >= 1e-7:
                flagg1 += 1
            if flagg1 == 0 and flags1 == 0:
                return [round(val, 5), round(ymid, 5), round(value, 5)], [i + 1, j + 1, k + 1, 1]
            if flagg1 + flagg2 + flagg3 + flagg4 > flags1 + flags2 + flags3 + flags4:
                value += dif
                dif = dif / 2
            else:
                value -= dif
                dif = dif / 2
            #print(value, dif)
            if dif < 1e-7:
                return [round(val, 5), round(ymid, 5), round(value, 5)], [i + 1, j + 1, k + 1, 1]


# print(main(2, [[(0, 25.5), (40.3, 70), (80, 95.1)], [(10, 40), (45, 55), (60, 78)]]))
# print(main(2, [[(0, 25), (75, 100)], [(12.5, 37.5), (62.5, 87.5)]]))
# print(main(4, [[(0, 50)], [(10, 34), (50, 70)], [(50, 60), (70, 90)], [(30, 70)]]))
# print(main(3, [[(0, 25), (75, 100)], [(12.5, 37.5), (62.5, 87.5)], [(37.5, 62.5)]]))
# print(main(4, [[(10, 35), (50, 68)], [(10, 35), (50, 68)], [(10, 35), (50, 68)], [(10, 35), (50, 68)]]))
# print(main(4, [[(0, 5), (10, 15), (50, 70), (90,100)], [(0, 15), (20, 35), (40, 55), (60, 67), (70, 74), (90,100)], [(3, 5), (8,10), (10, 15), (60, 80), (85,99)], [(50, 70), (90,100)]]))
# print(main(4, [[(0,5), (10,15), (20,25), (25, 30), (35,40), (50,60), (75,80), (90,100)], [(0,5), (10,15), (20,25), (25, 30), (35,40), (50,60), (75,80), (90,100)], [(0,5), (10,15), (20,25), (25, 30), (35,40), (50,60), (75,80), (90,100)], [(0,5), (10,15), (20,25), (25, 30), (35,40), (50,60), (75,80), (90,100)]]))
