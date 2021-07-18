value = [0,8,10,6,3,7,2]
weight = [0,4,6,2,2,5,1]
storage = 12
item = len(value) - 1

class solution:
    def __init__(self):

        self.back = []

        for __ in range(0,storage+1):
            self.back.append([0] * (item + 1))

    def deal(self, s, i):

        if weight[i] > s:
            return self.back[s][i-1]
        else:
            return max(self.back[s-weight[i]][i-1]+value[i], self.back[s][i-1])

    def main(self):

        for s in range(1,storage+1):
            for i in range(1,item+1):
                self.back[s][i] = self.deal(s,i)

        print(self.back)


solu = solution()
solu.main()