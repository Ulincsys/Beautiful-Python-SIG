class className:
    def __init__(self, x = None):
        self.x = x
        
        print(f"New instance initialized with value: {x}")
    
    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"Cannot compare {type(self)} with {type(other)}")
        
        return self.x < other.x
    
    def __int__(self):
        return self.x
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.x})"

o = className(10)
x = className(15)
print(o < x) # True

print(o) # className(10)
print(int(o)) # 10