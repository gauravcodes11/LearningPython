#defining and calling a function
def fun():
    print("hello")
fun()
#function arguments
def fun(x):
    if x%2==0:
        print("even")
    else:
        print("odd")
fun(7)
#default args
def fun(x=10,y=50):
    print("x:",x)
    print("y:",y)
fun(6)
#keyword args
def fun(name,age):
    print(name, age)
fun(name="hello", age=44)
fun(age=44,name="hello")
#positional arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")
#arbitrary args
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='jon', mid='von', last='neumann')# Function call with both types of arguments
#nested function
def f1():
    s = 'I love anime'
    def f2():
        print(s)
        
    f2()
f1()
#anonymus function
def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda #think of it as cube_l(x):x*x*x

print(cube(7))
print(cube_l(7))
#recursive functions
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))
