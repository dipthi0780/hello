#keyword and positional arguments

'''def Details(id,name,mailid):
    id = 10
    name = "Rachel"
    mailid = "rachel@gmail.com"
    print(id,name,mailid)
Details(id = "id", name = "name", mailid = "mailid")'''

'''def Details (id,name,mailid):
    print(id,name,mailid)
Details(id = "id", name = "name", mailid = "mailid")
Details (id = "1", name = "abc", mailid = "abc@gmail.com")
Details (2, "dfghj", "dfgh@gmail.com")
Details ("3","ghi", "ghi@gmail.com")
Details ( mailid = "jkl@gmail.com", id = "4",name = "jkl")'''

#swap numbers

#without using temp
a = 10
b = 20
'''a,b = b,a
print("a value is", a)
print("b value is", b)'''

#with temp
'''temp = a
a = b
b = temp
print("a value is", a)
print("b value is", b)'''

#using arthemetic
'''a = a+b
b = a-b
a = a-b
print("a value is", a)
print("b value is", b)'''

#using format
'''a = a+b
b = a-b
a = a-b
print("after swapping = a %d, b = %d"%(a,b))'''

#default arguments

'''def grocery(item,price):
    print("item is %s"%item)
    print("price is %d"%price)
grocery("sugar",100)'''

'''def grocery(item = "rice",price=1500):
    print("item is %s"%item)
    print("price is %d"%price)
grocery()'''

'''def grocery(item,price = 200):
    print("item is %s"%item)
    print("price is %d"%price)
grocery("dhal")'''

'''def grocery(item = "salt",price):
    #error - non def arg followed by def arg
    print("item is %s"%item)
    print("price is %d"%price)
grocery(210)'''

'''def bakery(cake,price,quantity):
    print("cake name is %s"%cake)
    print("price is %2f"%price)
    print("quantity is %s"%quantity)
bakery("vanilla",250, "100kg")

def bakery(cake = "pineapple",price = 100,quantity = "100kg"):
    print("cake name is %s"%cake)
    print("price is %2f"%price)
    print("quantity is %s"%quantity)
bakery()

def bakery(cake,price = 300,quantity = "250kg"):
    print("cake name is %s"%cake)
    print("price is %2f"%price)
    print("quantity is %s"%quantity)
bakery("strawberry")

def bakery(cake,price,quantity = "50"):
    print("cake name is %s"%cake)
    print("price is %2f"%price)
    print("quantity is %s"%quantity)
bakery("chocolate", 1000)'''

# * arguments (* is used to unpack the elements from  a dataset)

'''a = [3,4,5,6,7]
print(a)
print(*a)
print(type(a))'''

'''b = (3,4,5,6,7)
print(b)
print(*b)
print(type(b))'''

'''c = {3,4,5,6,7}
print(c)
print(*c)
print(type(c))'''

'''d = "{name" : "rachel", "month" : 2026}
print(d)
print(*d)
print(type(d))'''

'''e = "rachel"
print(e)
print(*e)
print(type(e))'''

'''a,b,c = 1,2,3,4,5,6,7
print(a)
print(b)
print(c)''' #error

'''a,b,c = 1,2,3
print(a)
print(b)
print(c)'''

'''a,b,c = 1,2,3,4,5,6,7
print(a)
print(b)
print(*c)'''

'''a,b,c = 1,2,3,4,5,6,7
print(a)
print(*b)
print(c)

a,b,c = 1,2,3,4,5,6,7
print(*a)
print(b)
print(c)

a*,b,c = 1,2,3,4,5,6,7
print(*a)
print(b)
print(c)

a,b,c = "rachel"
print(a)
print(b)
print(c) #error

a,b,c = "rac"
print(a)
print(b)
print(c)

a,*b,c = "rachel"
print(a)
print(*b)
print(c) '''
