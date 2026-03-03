Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversion
#int
int(4)
4
int(5.6)
5
int("hi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(4+6j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(4+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(5)
5.0
float(4.5)
4.5
float("hi")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(4+6j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(4+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#str
str(5)
'5'
str(8.9)
'8.9'
str("hi")
'hi'
str(3+8j)
'(3+8j)'
str(true)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    str(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
str(True)
'True'
str(False)
'False'
#str coverts all as python is string based
#complex
>>> complex(3)
(3+0j)
>>> complex(4.7)
(4.7+0j)
>>> complex("hi")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex("hi")
ValueError: complex() arg is a malformed string
>>> complex(4+8j)
(4+8j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(4)
True
>>> bool(2.5)
True
>>> bool("hi")
True
>>> bool(4+7j)
True
>>> bool(True)
True
>>> bool(False)
False
