Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=298
>>> type(a)
<class 'int'>
>>> b=5.67
>>> type(b)
<class 'float'>
>>> c="dipthi"
>>> type(c)
<class 'str'>
>>> d=5+8j
>>> type(d)
<class 'complex'>
>>> d=4j+578
>>> type(d)
<class 'complex'>
>>> x=True
>>> type(x)
<class 'bool'>
>>> y=false
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    y=false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> y=False
>>> type(y)
<class 'bool'>
