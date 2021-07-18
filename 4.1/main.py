def sum(li):
    if len(li)>1:
        x=li[0]
        li.pop(0)
        return x + sum(li)
    else:
        return li[0]

li=[3,6,1,5,98,1]
print(sum(li))