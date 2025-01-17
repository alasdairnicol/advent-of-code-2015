import itertools
lines = open("day09.txt").readlines()
distances = {(words[0], words[2]): int(words[-1]) for line in lines for words in [line.strip().split()]}
places = {p for pairs in distances for p in pairs}

def distance(ordering):
    return sum(distances.get((a,b), distances.get((b,a))) for (a,b) in itertools.pairwise(ordering))

print(min(distance(ordering) for ordering in itertools.permutations(places)))
print(max(distance(ordering) for ordering in itertools.permutations(places)))
