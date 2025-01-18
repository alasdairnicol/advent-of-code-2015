>>> def sum_obj(x, ignore_red=False):
...     if isinstance(x, str):
...         return 0
...     if isinstance(x, int):
...         return x
...     elif isinstance(x, list):
...         return sum(sum_obj(y, ignore_red=ignore_red) for y in x)
...     elif isinstance(x, dict):
...         if ignore_red and "red" in x.values():
...             return 0
...         return sum(sum_obj(y, ignore_red=ignore_red) for y in x.values())
...
>>> sum_obj(obj)
119433
>>> sum_obj(obj, ignore_red=True)
68466
