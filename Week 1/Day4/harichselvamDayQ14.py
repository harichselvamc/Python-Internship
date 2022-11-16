def double(integer):
    return integer*2

integerlist = [1, 2, 3]
outputlist = list(map(double, integerlist))
outputtuple = tuple(map(double, integerlist))

print(outputlist)
print(outputtuple)
