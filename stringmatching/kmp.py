def kmpstringmatch(pattern, txt, array):
    n = len(txt)
    i = 0
    j = 0
    index = []
    count = 0
    while i < n:
        if (pattern[j] == txt[i]):
            i += 1
            j += 1
        elif (j != 0):
            j = array[j - 1]
        else:
            i = i + 1
        if (j == len(pattern)):
            index.append(i - len(pattern))
            count += 1
            #             important step
            j = array[j - 1]

    return index


def Kmppreprocess(pattern):
    j = 0
    i = 1
    m = len(pattern)
    array = [0] * m
    while i < m:
        if (pattern[i] == pattern[j]):
            j = j + 1
            array[i] = j
            i = i + 1
        elif (j > 0 and pattern[i] != pattern[j]):
            j = array[j - 1]
            i = i + 1
        else:
            array[i] = 0
            i = i + 1
    return array


txt = "ABABDABACDABABCABABABCABAB"
pat = "ABABCABAB"
array = Kmppreprocess(pat)
kmpstringmatch(pat, txt, array)