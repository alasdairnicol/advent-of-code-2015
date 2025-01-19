>>> values = [int(x) for x in lines]
>>>
>>> import itertools
>>>
>>> total = 0
>>> for i in range(1, 21):
...     for c in itertools.combinations(values, i):
...         if sum(c) == 150:
...             total += 1
...
>>> total
1638

>>> for i in range(1, 21):
...     for c in itertools.combinations(values, i):
...         if sum(c) == 150:
...             total += 1
...     if total:
...         break
...
>>> total
17
