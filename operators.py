Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthimetic
a=6;b=5
print(a+b)
11
print(a-b)
1
print(a*b)
30
print(a/b)
1.2
print(a//b)
1
print(a%b)
1
#assignment
a=5;b=56
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
61
a-=b
a
5
a*=b
a
280
a/=b
a
5.0
a//=b
a
0.0
a%=b
a
0.0
b+=23
b
79
b-=a
b
79.0
b*=45
b
3555.0
b/=a
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    b/=a
ZeroDivisionError: division by zero
b//=23
b
154.0
b/=a
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    b/=a
ZeroDivisionError: division by zero
b/=2
b
77.0
b%=12
b
5.0
a**=b
a
0.0
b**=23
b
1.1920928955078124e+16


#comparison
a=76;b=87
a<b
True
a>b
False
b>a
True
b<a
False
a==b
False
a>=b
False
a<=b
True
b>=a
True

#logical
a=67;b=56
a>b and b>a
False
a<b and b<a
False
a!=b and a==b
False
a>b and a<b
False
a>b and a>b
True
a>b or b<a
True
a!=b or b==a
True
not true
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
a<=b or a>=b
True

#identify
a=34;b=45
a=34
if type(a) is int:
    print("no is int")

    
no is int
if type(a) is float:
    print("num is int")

    
if type(a) is not float:
    print("num is int")

    
num is int

#membership
a=2,3,4,5,6,7,8
if 5 in a:
    print(5)

    
5
if 34 in a:
    print(34)

    
if 34 not in a:
    print(34)

    
34

#bitwise
a=2;b=4
a&b
0
a=4;b=8
a&b
0
a=8;b=9
a&b
8
a=4;b=9
a&b
0
a=5;b=9
a!b
SyntaxError: invalid syntax
a|b
13
>>> a=2;b=8
>>> a|b
10
>>> bin(2)
'0b10'
>>> bin(8)
'0b1000'
>>> 
>>> a=3;b=4
>>> a~b
SyntaxError: invalid syntax
>>> a=3
>>> ~a
-4
>>> b=45
>>> ~b
-46
>>> 
>>> a=2;b=9
>>> a^b
11
>>> a=7;b=9
>>> a^b
14
>>> a=1;b=4
>>> a^b
5
