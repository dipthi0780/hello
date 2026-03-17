
#loops
#for,while,range(),break,continue,pass:

#for loop
'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''#error

'''a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=(3,4,5,6,7)
for i in a:
    print(i)
    print(type(a))
    print(type(i))

a={2,3,4,5,6,7,8,9}
for i in a:
    print(i)
    print(type(a))
    print(type(i))
for i in a.values():
    print(i)
    print(type(a))
    print(type(b))
for i in a.items:
    print(i)
    print(type(a))
    print(type(i))

a="codegnan"
for i in a:
    print(i,end=" ")
    print(type(a))
    print(type(b))'''

#print(a.upper())
'''b=str(a)
print(b.upper())

for i in a:
    print(i.upper(),end=" ")'''

#while loop:
'''a=4
b=6
while a<b:
    print(a)'''

'''a=5
while a>1:
    print(a)
    a=a-1'''

'''a=5
while a>1:
    print(a)
    a=a+1'''

'''a=5
while a>1:
    a=a-1
    print(a)'''

'''a=10
while a>1:
    print(a)
    a-=1

a=1
while a>1:
    print(a)
    a+=1'''
    
'''while True:
    num=int(input("enter value:"))
    if num%2==0:
        print("even")
    else:
        print("odd")'''

'''while True:
    a=int(input("enter year"))
    if a %4==0:
        print("leap year")
    else:
        print("not leap year")'''

#range:
#the range function return a sequence of numbers starting from ,0 by default and increments one by one and stops before a specified numbers
'''for i in range(5):
    print(i)'''

'''for i in range(10,20):
    print(i,end=",")'''

'''for i in range(0,20,2):
    print(i)'''

'''for i in range(5,50,5):
    print(i,end=",")'''


'''for i in range(3,30,3):
    print(i,end=",")'''

#task:
'''while True:
    i=int(input("enter a number:"))
    if i in range(91,101):
        print("grade A")
    elif i in range(81,91):
        print("grade B")
    elif i in range(71,81):
        print("grade C")
    elif i in range(50,71):
        print("grade D")
    elif i in range(0,51):
        print("fail")'''

#break:
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''
        

'''a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)'''

'''a=5
while a>=1:
    print(a)
    a=a-2
    if a==20:
        break'''

'''for i in range(25):
    if i==15:
        break
    print(i)'''

'''a="python"
if a=="t":
    break
print(a)'''#error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue:
'''a=20
while a>1:
    a=a-1
    if a==10:
        continue
    print(a)'''

'''for i in range(15):
    if i==12:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="t":
        continue
    print(i)'''

#pass:
'''a=15
while a>2:
    print(a)
    a=a-1
    if a==10:
        pass'''

'''for i in range(10):
    if i==3:
        pass
    print(i)'''

'''a="code"
for i in a:
    if i=="d":
        pass
    print(i)'''













































