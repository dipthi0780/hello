Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#len()
a="codegnan"
len(a)
8
a="python course"
len(b)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    len(b)
NameError: name 'b' is not defined
len(a)
13
a=""
len(a)
0
a=" "
len(a)
1
#count:
a="twinkle twinkel little star'
SyntaxError: unterminated string literal (detected at line 1)
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count("w")
2
a.count(" ")
3

#find a string:
a="python"
a[1]
'y'
a.find("n")
5
#consider first one no repetition:
b="codegnan"
b.find("n")
5
b[5]+b[7]
'nn'
#escape sequences:
#\n->new line
#\t->tab space
a="name\nmobilenum\temail id\ncity
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobile num\temail id\ncity"
print(a)
name
mobile num	email id
city
a="name:dipthi\nmobile num:7386150798\temail id:dipthi23@gamil.com\ncity:vijayawada"
print(a)
name:dipthi
mobile num:7386150798	email id:dipthi23@gamil.com
city:vijayawada
#replace:
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a="wait wait until you succeed"
a.replace("wait","work")
'work work until you succeed'
a.replace("wait","work",1)
'work wait until you succeed'

#upper:
a="hello"
a.upper()
'HELLO'
#lower
a="HI"
a.lower()
'hi'
b="python"
b.capitalize()
'Python'
c="python course"





















c.title()
'Python Course'
a="code"
a.isupper()
False
a.islower()
True
a.startswith("c")
True
a.endswith("e")
True
a.isalpha()
True
b="python course"
b.isalpha()
False
b.isdigit()
False
c="123455"
c.isdigit()
True
d="dipthi@123"
d.isalnum()
False
d="dipthi123"
d.isalnum()
True

#strip:
a="        dipthi        "
a.strip()
'dipthi'
a.lsrtip()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.lsrtip()
AttributeError: 'str' object has no attribute 'lsrtip'. Did you mean: 'lstrip'?
a.lstrip()
'dipthi        '
a.rstrip()
'        dipthi'
#split:
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
a="i am learning python"
a.split()
['i', 'am', 'learning', 'python']
a="python","java","c","c++"
"".join(a)
'pythonjavacc++'
" ".join(a)
'python java c c++'
"@".join(a)
'python@java@c@c++'
a="code"
b="gnan"
print(a+b)
codegnan
fname="dipthi"
lname="reddy"
print(fname+" "+lname)
dipthi reddy
print((fname+" "+lname).title())
Dipthi Reddy
#concatination

#formating:
a=3
b=5
print(a+b)
8
print("sum is",a+b)
sum is 8
c="dipthi"
print("name is",c)
name is dipthi

#format method:
a="motu"
b="patlu"
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu

#fstring:
a="ram"
b="sita"
print(f"hello {a}{b})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"hello {a}{b}")
      
hello ramsita
print(f"hello {a}
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"hello {a} hello {b}")
      
hello ram hello sita

#list[]:
      
a=[3,4.5,"python",6+8j,True,False]
      
print(a)
      
[3, 4.5, 'python', (6+8j), True, False]
type(a)
      
<class 'list'>
c=[9]
      
type(c)
      
<class 'list'>
a=["python","java","c","c++"]
      
a.append("html")
      
a
      
['python', 'java', 'c', 'c++', 'html']
#append take only one varaiable:
      
a.extend(["css","js"])
      
a
      
['python', 'java', 'c', 'c++', 'html', 'css', 'js']
a.insert(1,"ds")
      
a
      
['python', 'ds', 'java', 'c', 'c++', 'html', 'css', 'js']
a.insert(5,"sql")
      
a
      
['python', 'ds', 'java', 'c', 'c++', 'sql', 'html', 'css', 'js']

a=["apple","banana","cherry"]
      
a.index("grapes")
      
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    a.index("grapes")
ValueError: list.index(x): x not in list
a.index("cherry")
      
2
a.copy()
      
['apple', 'banana', 'cherry']
b=a.copy()
      
b
      
['apple', 'banana', 'cherry']
a.clear[]
      
SyntaxError: invalid syntax
a.clear()
      
a
      
[]
b=[]
      
b.append("c")
      
b
      
['c']
b.extend(["hi","hello"])
      
b
      
['c', 'hi', 'hello']
#pop
      
a=["hi
   
SyntaxError: unterminated string literal (detected at line 1)
a=["hi","hello","how","are","you"]
   
a.pop()
   
'you'
a
   
['hi', 'hello', 'how', 'are']
a.pop(2)
   
'how'
a
   
['hi', 'hello', 'are']
a=["java","ml","c","ai"]
   
a.sort()
   
a
   
['ai', 'c', 'java', 'ml']
a=[1,2,8,9,10,11,20,30]
   
a.sort()
   
a
   
[1, 2, 8, 9, 10, 11, 20, 30]

#reverse:
   
a=["white","red","pink","black"]
   
a.reverse()
   
a
   
['black', 'pink', 'red', 'white']
a=[1,2,8,9,10,11,20,30]
   
a.reverse()
   
a
   
[30, 20, 11, 10, 9, 8, 2, 1]

a=["html","java","js"]
...    
>>> a.pop("js")
...    
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    a.pop("js")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.remove("js")
...    
>>> a
...    
['html', 'java']
>>> a=["mango","banana","cherry"]
...    
>>> len(a)
...    
3
>>> c=["mango"]
...    
>>> c
...    
['mango']
>>> len(c)
...    
1
>>> c.count("mango")
...    
1
