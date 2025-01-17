def diff(word):
    w = iter(word)
    x = 0
    for c in w:
        x+=1
        if c == '\\':
            c = next(w)
            if c == 'x':
                 next(w)
                 next(w)
    return len(word) - x + 2

def extra(word):
    return 2 + word.count('"') + word.count('\\')

words = [line.strip() for line in open('day08.txt').readlines()]

print(sum(diff(w) for w in words))
print(sum(extra(w) for w in words))
