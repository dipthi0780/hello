def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i, a[i])
    for i in a.items():
        print(i)
check2()
details={"idnos":[10,20,30],
         "names":['priya', 'sita', 'raj'],
         "status":["P", "A", "P"]}
check2(**details)

def final(*a, **b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i, j in b.items():
        print("key is", i)
        print("value is", j)
final()
data=(2, 3, 4, 5, 4.3, 2.3)
