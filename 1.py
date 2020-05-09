#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.set_printoptions(linewidth=100000, threshold=np.inf)
x = np.linspace(-1, 6, 100)
# boundary
y1 = 2 * x + 2
y2 = 0.5 * x + 1
y3 = -x + 5
z = x + 3

# draw
top = np.where(y3 < y1, y3, y1)
bottom = y2
# 创建画布
fig = plt.figure(figsize=(8, 8))
# 创建一个绘图区对象
plt.plot(x, y1, 'g-')
plt.text(0.8, 5.5, "$2x_1-x_2=-2$")
plt.plot(x, y2, 'g-')
plt.text(0.2, 4.9, "$x_1-2x_2=2$")
plt.plot(x, y3, 'g-')
plt.text(3.5, 3.2, "$x_1+x_2=5$")
plt.plot(x, z, 'r-', linewidth='2')
plt.text(2.2, 5, "$-x_1+x_2=3$")
# plt.text(1.1, 4, "$(1, 4) Optimum$")
plt.scatter(1, 4, c='r', marker='o', )
plt.axis([0, 6, 0, 6])
plt.fill_between(x, bottom, top, where=top > bottom, facecolor='g', alpha=0.1)
plt.annotate("$(1, 4) Optimum$", (1, 4), (1.2, 4))
plt.savefig('./test1.jpg')
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.title("Feasible Domain")

plt.show()
print(0)
