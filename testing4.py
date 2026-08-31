ls = ["a", "b", "c", "d"]
ls2 = ["e", "f", "g", "h"]


for i, letter in enumerate(ls):
    print(f"i: {i}\tletter: {letter}")


print("-" * 100)

for l1, l2 in zip(ls, ls2):
    print(f"l1: {l1}\tl2: {l2}")


ls3 = [[j for j in range(10)] for i in range(10)]
ls4 = [0] * 10
print(ls4)


print("-" * 100)


def bitmask(mask):
    subset = mask
    while subset:
        subset = mask & (subset - 1)


print(bitmask(18))
