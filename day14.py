>>> lines = open("day14.txt").readlines()
>>> def parse_line(line: str):
...     words = line.split()
...     speed = int(words[3])
...     fly_time = int(words[6])
...     rest_time = int(words[13])
...     return speed, fly_time, rest_time
...
>>> def distance_after(seconds, speed, fly_time, rest_time):
...     quotient, remainder = divmod(seconds, fly_time + rest_time)
...     extra_seconds = min(fly_time, remainder)
...     return speed * (quotient * fly_time + extra_seconds)
...
>>> seconds = 2503
>>> max(distance_after(seconds, *parse_line(line)) for line in lines)
2696

reindeer = [parse_line(line) for line in lines]
points = [0 for l in lines]
>>> for second in range(1, seconds + 1):
...     distances = [distance_after(second, *r) for r in reindeer]
...     max_distance = max(distances)
...     for i, d in enumerate(distances):
...         if d == max_distance:
...             points[i] += 1
...
print(max(points)
