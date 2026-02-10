# File name is "romeo.txt"
fajl = raw_input("unesite ime fajla:")
fajlOpen = open(fajl)
listica = []
linije = [line.split() for line in fajlOpen]
for i in linije:
    for j in i:
        if j not in listica:
            listica.append(j)
listica.sort()
print(listica)



