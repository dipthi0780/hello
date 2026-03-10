Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="vijayawada"
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a="life is beautiful"
a[5]+a[6]
'is'
a[8]+a[9]+a[10]+a[11]+a[12]+a[13]+a[14]+a[15]+a[16]
'beautiful'
a="i am in class"
a[0]
'i'
a[2]+a[3]
'am'
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a="simple is better"
a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'

#negative:
a="i love python"
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
a[-11]+a[-10]+a[-9]+a[-8]
'love'
a="vijayawada is a royal city"
a[-15]+a[-14]
'is'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'al city'
a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
a[-4]+a[-3]+a[-2]+a[-1]
'city'

#slicing;
a="codegnan"
a[0:4]
'code'
a[4:8]
'gnan'
a=[:4]
SyntaxError: invalid syntax
a[:4]
'code'
a[4:]
'gnan'

a="codegnan it solutions"
a[9:11]
'it'
a[4:8]
'gnan'
a[11:]
' solutions'
a[12:]
'solutions'

#negative:
a="work until you succeed"
a[-17:-12]
'until'
a[-22:-19]
'wor'
a[-22:-18]
'work'
a[-7:]
'succeed'
a="time is very precious"
>>> a[-13:-9]
'very'
>>> a[-21:-17]
'time'
>>> a[-8:]
'precious'
>>> 
>>> #striding:
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::4]
'd e'
>>> a="python development"
>>> a[::3]
'ph voe'
>>> a[::5]
'pnee'
>>> a[:3:]
'pyt'
>>> a[::2]
'pto eeomn'
>>> a[1:5:8]
'y'
>>> a[3:4:6]
'h'
