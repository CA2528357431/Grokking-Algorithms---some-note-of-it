ha = {'a': {'b': 5, 'c': 1}, 'b': {'e': 10}, 'c': {'d': 5, 'f': 6}, 'd': {'e': 3},
      'e': {'h': 3}, 'f': {'g': 2}, 'g': {'h': 10}}

dis = {'b': 5, 'c': 1}

back = {'b': 'a', 'c': 'a'}

used = []


def seek(dis):
    smv = 10000
    smk = None
    for key in dis:
        if key not in used:
            if dis[key] < smv:
                smv = dis[key]
                smk = key
    return smk


def do():
    while True:
        minor = seek(dis)

        if minor=='h':
            break

        used.append(minor)

        dis_base = dis[minor]
        for x in ha[minor]:
            dis_neo = ha[minor][x] + dis_base
            if x not in dis:
                dis[x] = dis_neo
                back[x] = minor
            else:
                if dis_neo < dis[x]:
                    dis[x] = dis_neo
                    back[x] = minor

do()
print(dis['h'])


down = 'h'
trace = [down]
while True:
    up = back[down]
    trace.append(up)
    if up == 'a':
        break
    down = up
trace.reverse()
print(trace)
