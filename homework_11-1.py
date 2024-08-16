import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import make_dataclass

r = requests.get('https://api.github.com/events')
print(f'r.encoding: {r.encoding}')
r1 = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(f'r1.text:\n{r1.text}')
r2 = requests.head('https://httpbin.org/get')
print(f'r2:\n {r2}\n\n\n')

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'a:\n {a}')
print(f'a.ndim:\n {a.ndim}')
print(f'a.shape:\n {a.shape}')
print(np.linspace(0, 21, num=8, dtype=np.int64))
print(f'{np.arange(4, 33, 4)}\n\n\n')

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s)

df = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
print(df)



Point = make_dataclass("Point", [("x", int), ("y", int)])

print(pd.DataFrame([Point(1, 1), Point(2, 3), Point(7, 5)]))

fig, ax = plt.subplots()
ax.plot([1, 1.5, 2, 2.5, 3, 4], [3.5, 1.5, 1, 2.5, 2, 3])
plt.show()







