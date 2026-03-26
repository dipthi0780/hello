#fromkeys:
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"dipthi")
print(b)
b["o"]="reddy"
print(b)'''

#evaluate[eval]():
'''while True
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    print(a+b)

    a=float(input("enter a value"))
    b=float(input("enter b value"))
    print(a+b)

    a=input("enter a value")
    b=input("enter b value")
    print(a+b)

    a=eval(input("enter a value"))
    b=eval(input("enter b value"))
    print(a+b)'''

#ZIP():
#we can combine multiple collections into one collection:
'''a=[10,20,30,40,50]
names=["dipthi","prithi","cherry","pavi","neha"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)'''

#enumerate()->we can give counter to the collection:
'''names=["dipthi","prithi","cherry","pavi","neha"]
#for i in range(len(names)):
#   print(i,names[i])
b=list(enumerate(names))
print(b)

b=list(enumerate(names,100))
print(b)

b=tuple(enumerate(names))
print(b)

b=set(enumerate(names))
print(b)

b=dict(enumerate(names))
print(b)'''




























