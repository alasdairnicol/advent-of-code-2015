>>> def parse_line(line):
...     words = line.strip(".\n").split()
...     amount = int(words[3])
...     if words[2] == "lose":
...         amount = -amount
...     return (words[0], words[-1]), amount
...
>>> lines = open("day13.txt").readlines()
>>> pairs = dict(parse_line(line) for line in lines)
>>> people = {person for pair in pairs for person in pair}
>>> max(sum(pairs[a,b] + pairs[b,a] for a,b in itertools.pairwise(ordering + (o\
rdering[0],))) for ordering in itertools.permutations(people))
664
>>> max(sum(pairs[a,b] + pairs[b,a] for a,b in itertools.pairwise(ordering)) fo\
r ordering in itertools.permutations(people))
