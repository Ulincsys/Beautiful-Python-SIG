import numpy

arr = numpy.array(range(10))
starr = numpy.array(["a", "list", "of", "strings"])

print(arr)
print(starr)

try:
    arr[5] = "A String"
except Exception as e:
    print("Cannot insert string into int array")
    arr[5] = 100
    
try:
    starr[5] = 100
except Exception as e:
    print("Cannot insert int into string array")
    starr[2] = "A String"

print(arr)
# Note the truncation
print(starr)