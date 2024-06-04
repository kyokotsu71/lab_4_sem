from itertools import permutations

word = "комбинаторика"
res = set(permutations('комбинаторика', 4))
print(res)
print(len(res))

