file = open('C:\New folder', 'r+')
# file = open(r'C:\New folder', 'r')
#print(file.readlines())
v = []
for elem in file:
    v.append(elem)
print(v)
file.seek(0)
v = file.readlines()
flg5 = 0
for i in range(len(v)):
    if v[i].startswith('5'):
        flg5 = 1
    if v[i].startswith('6'):
        if flg5 == 0:
            v.insert(i, '5555\n')
        break
print(v)
file.seek(0)
file.writelines(v)
print(file.tell())
file.close()
file = open(r'C:\New folder', 'r+')
line = file.readline()
while line != "":
    print(line)
    pos = file.tell()
    print(pos)
    if pos == 30:
        file.seek(30)
        file.write('3636')
    line = file.readline()
file.close()

file = open(r'C:\New folder', 'r+')
lines = file.read()
final = lines[:lines.find('6')] + '5555\n' + lines[lines.find('6'):]
print(final)
file.seek(0)
file.write(final)
file.close()