file = open("a.txt", "w") os f2
f2.write ('та запись должна появиться в доке А \')
print("вторая надпись", file=f2)
s=f2.readline()
print(s)
file.close