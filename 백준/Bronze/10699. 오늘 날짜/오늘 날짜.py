import datetime as dt

g = dt.datetime.now().month
if(g<10):
    g = '0'+str(g)
else:
    g = str(g)

h = dt.datetime.now().day
if(h<10):
    h = '0'+str(h)
else:
    h = str(h)
print(str(dt.datetime.now().year) + '-' + g + '-'+h)
