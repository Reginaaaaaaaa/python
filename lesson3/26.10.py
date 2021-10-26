import time
import random
import matplotlib.pyplot as plt

def bubble(inp_list):
    for i in range(len(inp_list)):
        for k in range(len(inp_list)-1-i):
            if inp_list[k] > inp_list[k+1]:
                inp_list[k], inp_list[k+1] = inp_list[k+1], inp_list[k]

def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index


time_list, n_list = [], []
time_list_2, n_list_2 = [], []
for n in range(100, 2000, 100):
    elements = [random.randrange(0, n) for _ in range(n) ]
    t = time.time()
    bubble(elements)
    work_time = time.time() - t
    time_list.append(work_time)
    n_list.append(n)

    t_2 = time.time()
    BinarySearch(elements, n)
    work_time = time.time() - t_2
    time_list_2.append(work_time)
    n_list_2.append(n)

    print(n)

fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.plot(n_list, time_list)
ax2.plot(n_list_2, time_list_2)
plt.show()
