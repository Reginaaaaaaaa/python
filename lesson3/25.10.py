import matplotlib.pyplot as plt
# import numpy as np

# lag = 0.1
# x = np.arange(0.0, 2*np.pi+lag, lag)
# y = np.cos(x)

# fig = plt.figure()
# plt.plot(x, y)

# plt.text(np.pi-0.5, 0,  '1 Axes', fontsize=26, bbox=dict(edgecolor='w', color='w'))
# plt.text(0.1, 0, '3 Yaxis', fontsize=18, bbox=dict(edgecolor='w', color='w'), rotation=90)
# plt.text(5, -0.9, '2 Xaxis', fontsize=18, bbox=dict(edgecolor='w', color='w'))

# plt.title('1a TITLE')
# plt.ylabel('3a Ylabel')
# plt.xlabel('2a Xlabel ')

# plt.text(5, 0.85, '6 Xticks', fontsize=12, bbox=dict(edgecolor='w', color='w'), rotation=90)
# plt.text(0.95, -0.55, '6 Xticks', fontsize=12, bbox=dict(edgecolor='w', color='w'), rotation=90)

# plt.text(5.75, -0.5, '7 Yticks', fontsize=12, bbox=dict(edgecolor='w', color='w'))
# plt.text(0.15, 0.475, '7 Yticks', fontsize=12, bbox=dict(edgecolor='w', color='w'))

# plt.grid(True)

import time
import random

 
def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n>q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)
 
 
times1, ns1 = [], []


times, ns = [], []

for n in range(200, 4000, 100):
    elements = [random.randrange(0, n) for _ in range(n)]
    t = time.time()
    bubble(elements)
    work_time = time.time() - t
    times.append(work_time)
    ns.append(n)
    t1 = time.time()
    quicksort(elements)
    work_time1 = time.time()- t1
    times1.append(work_time1)
    ns1.append(n)
    print(n)

fig, ax= plt.subplot()
ax1 = ax.twinx()
ax.plot(ns, times)
ax1.plot(ns1, times1)
plt.show()