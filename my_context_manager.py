class SimpleContextManager:
    def __init__(self):
        print("Initialized manager")
        
    def __enter__(self):
        print("Entered context")
    
    def __exit__(self, exception_type, exception_object, exception_traceback):
        if exception_type:
            print(f"Exited context with exception: {exception_type}({exception_object})")
            # Return True to stop the exception from propagating to the calling context
            return True
            # Return nothing to allow the exception to be caught in the calling context
        else:
            print("Exited context without exception")

with SimpleContextManager() as s:
    print("In context")
    raise TypeError("Haha")