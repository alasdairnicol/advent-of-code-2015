properties = [[int(x) for x in re.findall(r'(-?\d+)', line)] for line  in l\
ines]

>>> max_score = 0

>>> for ingredient_1 in range(0, 101):
...     for ingredient_2 in range(1, 101):
...         if ingredient_1 + ingredient_2 > 100:
...             break
...         for ingredient_3 in range(1, 101):
...             if ingredient_1 + ingredient_2 + ingredient_3 > 100:
...                 break
...             ingredient_4 = 100 - (ingredient_1 + ingredient_2 + ingredient_3)
...             ingredients = [ingredient_1, ingredient_2, ingredient_3, ingredient_4]
...             total_properties = [[i*x for x in property] for i, property in zip(ingredients, proper\
ties)]
...             zipped = list(max(0, sum(z)) for z in zip(*total_properties))
...             max_score = max(max_score, math.prod(zipped[:-1]))
...

# Now, only update max_score when calories is 500
>>> max_score = 0
>>> for ingredient_1 in range(0, 101):
...     for ingredient_2 in range(1, 101):
...         if ingredient_1 + ingredient_2 > 100:
...             break
...         for ingredient_3 in range(1, 101):
...             if ingredient_1 + ingredient_2 + ingredient_3 > 100:
...                 break
...             ingredient_4 = 100 - (ingredient_1 + ingredient_2 + ingredient_3)
...             ingredients = [ingredient_1, ingredient_2, ingredient_3, ingredient_4]
...             total_properties = [[i*x for x in property] for i, property in zip(ingredients, proper\
ties)]
...             zipped = list(max(0, sum(z)) for z in zip(*total_properties))
...             if zipped[-1] == 500:
...                 max_score = max(max_score, math.prod(zipped[:-1]))
...
>>> max_score
