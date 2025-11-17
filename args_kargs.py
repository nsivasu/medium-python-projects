def greet(*args,**kwargs):
    for arg in args:
        print("Hi!",arg)
    
    for i, val in kwargs.items():
        print(f"key:{i}  Value: {val}")

greet("Ann","Bob", a=25, b="Lian")