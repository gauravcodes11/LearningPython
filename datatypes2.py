# Set
s=set((1,2,"shonen"))
print(s)
print(type(s))

#s1=set((56565)) gives error as int is not iterable.
s1=set(("gauravupreti")) #iterates the string removing the dupicate values
print(type(s1))
print (s1)

s2={"gaurav"} # prints string
print(s2)

#access the elements
s3={"ram", "bharat", "mohan", "ram"}
print(s3)

for i in s3:
    print(i, end=" ") #prints items one by one


print("ram" in s3)  

# dictionary

d = {1: 'Gaurav', 2: 'Suresh', 3: 'Ramesh'}
print(d)

#Accesing key-value 
d = {1: 'Gaurav', 'name': 'Dehradun', 2: 'Raghu'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(2))

a=None
print(type(a))