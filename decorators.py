def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet():
    print("Hello, World!")
greet() 

#four properties of a function
    # Assigning a function to a variable
def greet(n):
    return f"hello, {n}!"
say_hi=greet
print(say_hi("alex"))
    # Passing a function as an argument
def apply(f, v):
    return f(v)
res = apply(say_hi, "Elon")
print(res) 
    # Returning a function from another function
def make_mult(f):
    def mult(x):
        return x * f
    return mult
dbl = make_mult(2)
print(dbl(5))

#chaining multipe decorators
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())