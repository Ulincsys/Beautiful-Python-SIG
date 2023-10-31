from functools import wraps

def fun(i: int):
    if i < 0 or i > 100:
        return
    ...
    
def fun2(i: int):
    if not isinstance(i, int):
        return
    
    if i < 0 or i > 100:
        return
    ...

def verify_i(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "i" in kwargs:
        # 'i' was passed by name, as opposed to place
            i = kwargs["i"]
            
        elif len(args) > 0:
        # We know that 'i' is the first argument
        # So it must be here if it's not in kwargs
            i = args[0]
            
        else:
        # We didn't find 'i'
            raise TypeError(f"{func.__name__}() missing 1 required positional argument: 'i'")
        
        if isinstance(i, int):
            if i < 0 or i > 100:
                return
            
            # We've verified 'i' is valid, so call func
            return func(*args, **kwargs)
    
    return wrapper

# def requires_i(i):
#     print(i)

# requires_i = verify_i(requires_i)

@verify_i
def requires_i(i):
    print(i)

print(requires_i.__name__)

requires_i(100)