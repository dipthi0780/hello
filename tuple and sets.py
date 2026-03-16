Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list is mutable:
#tuple():
#tuple is immutable:
a=(2,4.5."c",7+8j,True,False)
SyntaxError: invalid syntax
a=(2,4.5,"c",7+8j,True,False)
print(a)
(2, 4.5, 'c', (7+8j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.index(True)
4
a.count(4.5)
1

#sets{}:
#it is semimutable, dosent allow duplicatesa
a={2,5.7,"pooja",6+9j,True,False}
print(a)
{False, True, 'pooja', 2, (6+9j), 5.7}
b={1,2,5,3,0,7}
print(b)
{0, 1, 2, 3, 5, 7}
type(a)
<class 'set'>
a={1,2,3,4,5,6}
b={4,5,6}
a.add(20)
a
{1, 2, 3, 4, 5, 6, 20}
a.issubset(b)
False
b.issubset(a)
True
a={3,4,5,7,8}
b={2,3,4,5,9}
a.issuperset(b)
False
b.issuperset(a)
False
a={1,2,34,5,6,7,8}
b={5,6,7}
a.issuperset(b)
True

#union()
a={1,2,3,4,5,6,7}
b={4,5,6,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a={1,2,3,4,5,6,7}
b={3,4,5,6,7,8,9}
a.intersection(b)
{3, 4, 5, 6, 7}
a={1,2,3,4,5,6,7,8}
b={6,7,8,9,7}
a.difference(b)
{1, 2, 3, 4, 5}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a=
SyntaxError: invalid syntax

a={1,2,3,4,5,6,7,8,9}
b={4,5,6,8,9}
a.intersection_update(a)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.intersection_update(b)
a
{4, 5, 6, 8, 9}
b.intersection_update(a)
b
{4, 5, 6, 8, 9}

a={1,2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.difference_update(b)
a
{1, 2, 3, 4}
b.difference_update(a)
b
{5, 6, 7, 8, 9, 10, 11}
a={1,2,3,4,5,6}
b={3,4,5,6}
a.difference_update(b)
a
{1, 2}
a={1,2,3,4,5,6}
b={0,1,2,3,4,5,6}
a.difference_update(b)
a
set()

a={3,4,5,6,7,8}
b={1,2,3,4,5,6,7,8}
a.symmetric_difference(b)
{1, 2}
b.symmetric_difference(a)
{1, 2}
a.symmetric_difference_update(b)
a
{1, 2}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8}

a={1,3,5,7,9}
b={10,20,30,40}
a.pop()
1
a.remove(5)
a
{3, 7, 9}
b.pop()
40
b.remove(30)
b
{10, 20}
a={1,2,3,4,5,6,7}
a.copy()
{1, 2, 3, 4, 5, 6, 7}
a.clear()
a
set()
b=set
b.add(30)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    b.add(30)
TypeError: descriptor 'add' for 'set' objects doesn't apply to a 'int' object
>>> b=set()
>>> b.add(30)
>>> b
{30}
>>> a={1,2,3,4,5,6,7}
>>> a.discard(5)
>>> a
{1, 2, 3, 4, 6, 7}
>>> len(a)
6
>>> a={4,5}
>>> b={5,6}
>>> a.isdisjoint(b)
False
>>> a={1,2,3}
>>> b={6,7,8}
>>> a.isdisjoint(b)
True
>>> 
>>> #dictonaries:
>>> #dict{}:
>>> a={"name":"dipthi","year":2026,"month":3}
>>> print(a)
{'name': 'dipthi', 'year': 2026, 'month': 3}
