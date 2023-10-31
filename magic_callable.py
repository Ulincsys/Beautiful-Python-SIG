class my_callable:
    def __call__(self):
        print("Hello!")

o = my_callable()

print(callable(o)) # True

o() # Hello!