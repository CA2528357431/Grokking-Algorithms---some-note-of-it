class solution:
    def __init__(self, tar, ran):
        self.tar = tar
        self.ran = ran
        self.li = []
        for x in range(0, ran):
            self.li.append(x)

    def do(self, d, u):
        down = d
        up = u
        guess = (down + up) // 2
        if down > up:
            return " n o "

        if guess == self.tar:
            return self.tar
        elif guess > self.tar:
            return self.do(down, guess - 1)
        else:
            return self.do(guess + 1, up)


import time

qu = solution(99999999, 100000000)
t1 = time.time()

print(qu.do(0, qu.ran))

t2 = time.time()
print(t2 - t1)



'''
t3=time.time()
for x in range(qu.ran):
    if x==qu.tar:
        print(x)
        break
else:
    print( " n o " )
t4 = time.time()
print(t4-t3)
'''
