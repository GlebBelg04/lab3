l = list ('12345')
#l = + [10]
l.pop(2)
print(l)
s = set("12345")
s.add("6")
s.discard("3")
print(s)
z = dict(zip(l,s))
z["10"]="20"
del z ["5"]
print (z)

#l.remove("3")
print(l)
help(l)