
l = list((3,4,5,3,22,44))
print(type(l))
print (l)
for i in range (5):
    l = l + [1,1,1]
print (l)
l.remove(3)
print (l)

d = {'tree':2, 'wwkkwkk':1, 'golden':55, 'stage':32}
print (type(d))
print (d)
del d ['wwkkwkk']
print (d)
a = int(input("number"))
if a > 1:
    d['xiexie'] = 3
elif a < 1:
    d['fafa'] = 3
else:
    d['ahdie'] = 3
print (d)

S = set(l)
print(type(S))
print(S)
S.add(23)
print (S)
S.discard(4)
try:
    S.discard(3)
except: BaseException
print (S)