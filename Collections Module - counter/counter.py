from collections import Counter
l = [1, 1, 1, 1, 12, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
print(Counter(l))

s = 'assssvavavasvsbsbsbsbbaba'
print(Counter(s))

s = 'How many times does each word show up in this sentence word word shoe up up show'
words = s.split()
print(Counter(words))
c = Counter(words)
print(c.most_common(3))

# Common patterns when using the Counter() object
"""
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(lis_of_pairs))     # convert from a list of (elem,cnt) pairs
c.most_common()[:n-1:-1]        # n least common elements
c += Counter()                  # remove zero and negative counts
"""
print(sum(c.values()))