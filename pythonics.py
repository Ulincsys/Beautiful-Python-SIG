
# Not pythonic
l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
i = 0
while i < len(l):
    l[i] *= 2
    i += 1

# More pythonic
for i in range(len(l)):
    l[i] *= 2

for index, element in enumerate(l):
    l[index] = element * 2

l = [x * 2 for x in l]

l = list(map(lambda x: x * 2), l)

def really_long_function(
        index, list, count, four, five,
        columbia, chair, computer, table):
    pass

d = {
    "one_key": 5,
    "another": [
        
    ]
}