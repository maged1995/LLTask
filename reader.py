import re

l = []

sc = ec = sr = er = None

with open('receipt_sample.txt', 'r') as reader:
    for index, line in enumerate(reader.readlines()):
        s = list(re.finditer('\S+', line))
        if s and not ():
            if not sr:
                sr = index + 1
            if not sc or s[0].span()[0] < sc:
                sc = s[0].span()[0]
            if not ec or s[-1].span()[1] > ec:
                ec = s[-1].span()[1]
        elif sc != None:
            er = index + 1
            l.append([sc, ec, sr, er])
            sc = ec = sr = er = None
        else:
            print(sc)
            print('lb')
    else:
        if sc:
            er = index + 2
            l.append([sc, ec, sr, er])

print(l)