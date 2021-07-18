stations = {"kone": {"id", "nv", "ut"}, "ktwo": {"wa", "id", "mt"}, "kthree": {"or", "nv", "ca"}, "kfour": {"nv", "ut"},
            "kfive": {"ca", "az"}}

tar = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
base = []


def do():

    done = set()

    while True:

        choice = None
        out = 0
        for x in stations:
            if len(stations[x] - done) > out:
                out = len(stations[x] - done)
                choice = x

        if not choice:
            break

        done = done | stations[choice]
        base.append(choice)
        stations.pop(choice)

    return base


print(do())
