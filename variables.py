Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=23
print(a)
23
b=23
print(b)
23
print(a+b)
46
x=78
print(X)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
78
#python is case sensitive
#two variables at a time
a=10,b=40
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=10;b=40
print(a+b)
50
2=10
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
#donot start variable as a number:
a2=10
print(a2)
10
a0123456=56789955646
print(a0123456)
56789955646
name="Dipthi"
print(name)
Dipthi
print("name")
name
#it print the value in "",so dont use ""
_a=30
print(_a)
30
#_is a special character can be used anyways
_=40
print(_)
40
#del
a=10
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a2'?
a=10
print(a)
10
#other special characters should br given in strings
email=dipthid28@gmail.com
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    email=dipthid28@gmail.com
NameError: name 'dipthid28' is not defined
eamil="dipthid28@gmail.com"
print(email)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(email)
NameError: name 'email' is not defined. Did you mean: 'eamil'? Or did you forget to import 'email'?
mail="dipthid28@gmail.com
SyntaxError: unterminated string literal (detected at line 1)
'?
mail="dipthid28@gmail.com"
SyntaxError: unterminated string literal (detected at line 1)
mail="dipthid28@gmail.com"
print(mail)
dipthid28@gmail.com
>>> fname="dipthi"
>>> lname="reddy"
>>> print(fname+" "+lname)
dipthi reddy
>>> print(fname,lname)
dipthi reddy
>>> FIRST_name="dipthi"
>>> LAST_name="reddy"
>>> print(FIRST_name,LAST_name)
dipthi reddy
>>> name="dipthi"
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'name'?
>>> print(name)
dipthi
>>> x=30
>>> print(x)
30
>>> y=90
>>> print(x)
30
>>> if=80
SyntaxError: invalid syntax
>>> #donot start with key words
