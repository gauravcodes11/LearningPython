# taking input in python
name = input("Enter your name: ")
print("Hello,", name)   #printing output

# taking multiple inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# Taking input as int
n = int(input("How many roses?: "))
print(n)

# finding data type of input
a="hello world"
b=25
c=3.0
print(type(a))
print(type(b))
print(type(c))

# printing multiple outputs
name = "gaurav"
age = 25
city = "Dehradun"
print(name, age, city)