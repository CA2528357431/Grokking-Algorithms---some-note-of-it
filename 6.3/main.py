ha = {'a': ['a1', 'a2', 'a3', 'b2', 'x'], 'b': ['b1', 'b2', 'b3', 'c3', 'a'], 'c': ['c1', 'c2', 'c3', 'e2'],
      'd': ['d1', 'd2', 'd3', 'a1'], 'e': ['e1', 'e2', 'e3', 'b2'],
      'x': ['a', 'b', 'c'], 'y': ['c', 'd', 'e'],
      'o': ['x', 'a', 'y'],
      'a1': [], 'a2': [], 'a3': [], 'b1': [], 'b2': [], 'b3': [],
      'c1': [], 'c2': [], 'c3': [], 'd1': [], 'd2': [], 'd3': [],
      'e1': [], 'e2': [], 'e3': []
      }


def so(sb, tar):
    searched = []
    queue = ha[sb]
    while queue:
        obj = queue[0]
        queue.pop(0)
        if obj not in searched:
            searched.append(obj)
            if obj == tar:
                return 'yes'
            else:
                queue.extend(ha[obj])
    return 'no'


print(so('a', 'a'))
