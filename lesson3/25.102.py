import matplotlib.pyplot as plt
import xml.etree.ElementTree as et 

tree=et.ElementTree(file='d:\\Python\\menu.xml')
root = tree.getroot()
colors = ['r', 'g', 'b']
fig = plt.figure()
plt.ylabel('Prices, $')
plt.xlabel('Dishes')
i = 0
bar_colors = []
prices = []
names = []

for childe in root:
    color = colors[i]
    for gc in childe:
        bar_colors.append(color)
        prices.append( float(gc.attrib['price'][1:]))
        names.append(gc.text)
    if i == len(colors)-1:
        i = 0
    else:
        i += 1

bars = plt.bar(names, prices)
for i in range(len(bars)):
    bars[i].set_color(bar_colors[i])

plt.title('Menu prices')
plt.grid(True)
plt.show()



