#list comprehension:
a=["codegnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]
#print(a.upper()) error
'''b=str(a)
print(b.upper())'''

'''for i in a:
print(i.upper(),end=" ")'''

#syntax
#a=[exp for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

#task:
'''a=["vja","hyd","vzg"]
c=[d.title() for d in a]
print(c)'''

'''a=[2,4,5,6,8,12,13]
b=[x*x for x in a]
print(b)
b=[i**2 for i in a]
b=[pow(i,2) for i in a]
print(b)'''

#if-usage in list comprehension:
'''b=[i for i in range(16) if i%2==0]
print(b)'''#even

'''b=[i for i in range(16) if i%2!==0]
print(b)'''#odd

'''b=[i*i for i in range(16) if i%2==0]
print(b)'''#square

'''fruits=["apple","banana","mango","kiwi","berry","grapes"]
b=[i for i in fruits if 'a' in i]
print(b)'''

#no elif usage in list comprehension
#if else usage in list comprehension:

'''b=[i*i if i%2==0 else i*5 for i in range(21)]
print(b)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
c=[a[i]+b[i] for i in range(5)]
print(c)'''

#max,min,sum:
'''print(max(3,4,5,6,10,30,40))

print(min(3,4,5,6,10,30,40))

a=2,3,4,5,6,7,8,9,10
print(sum(a))
print(sum([1,2,3,4,5,6]))'''

#task:
print("-----student marks analysis report-----")
n=int(input("Enter total number of students:"))
marks=[int(input(f"enter marks of students{i+1}: ")) for i in range(n)]
total=sum(marks)
average=total/n if n>0 else 0
highest=max(marks) if n>0 else 0
lowest=min(marks) if n>0 else 0
print("marks:",marks)
print("total marks:",total)
print("average marks:",average)
print("highest marks:",highest)
print("lowest marks:",lowest)





















