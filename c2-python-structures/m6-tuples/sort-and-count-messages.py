count = 0
fname = input("Enter a file name:")
fhand = open(fname)
list1 = list()
dict1 = dict()
for line in fhand:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
            count = count + 1
            words = line.split()
            str1 = ''.join(words[5])
            list1.append(str1[0:2])
for word in list1:
    dict1[word] = dict1.get(word,0) + 1
for i,y in sorted(dict1.items()):
    print(i,y)


