#f.read(n)- читает н символ и записывает в строку, если н не дано читает до конца
#f.readline()- читает строку файла, записывает в файл
#f.readlines() - читает все строки файла,записывает в список [список строк]
#f.readble() - показывает тру или фолз(можно читать из файла или нельзя)

#f.write(строка) - записывает строку в файл
#f.writelines([string]) записывает список строк по очереди
#f.writeable() - можем записывать или нет


#1
f = open('D:\\Python\\worrk.txt', 'r')
print(f.read())
f.close


#2
f = open('D:\\Python\\worrk.txt','w')
f.write('New string')
f.close

f = open('D:\\Python\\worrk.txt', 'r')
print(f.read())
f.close


#3
f = open('D:\\Python\\worrk.txt', 'a')
f.write('\tNew String again')
f.close

f = open('D:\\Python\\worrk.txt', 'r')
print(f.read())
f.close

#4
f = open('D:\\forpython\\readme.txt', 'r')
g = f.readlines()
print(g)
f.close

#5
f = open('D:\\forpython\\readme.txt', 'w+')
h = f.writelines(['Ahmatova\n\t','1943'])
print(h)
f.close

#6
f = open('D:\\forpython\\fgd.txt', 'r+')
t = f.readlines()
t = [line[:-1] for line in t]
d = {t[1]:t[2], t[3]:int(t[4])}
print(d)
f.close