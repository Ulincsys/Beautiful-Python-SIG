from pathlib import Path

d = {"this is": "a dict"}
p = Path("file.txt")

print(str(d) == repr(d)) # True

# Prints the filename being pointed to
print(str(p))
# Prints the *type* of object as well
print(repr(p))