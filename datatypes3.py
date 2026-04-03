#multi line string
s="""i am going
home
let's meet tomorrow"""
print (s)

#accessing index
str="wassup"
print(str[-2])
print(str[3])

#string slicing
str1="cricket is popular"
print(str1[0:7])
print(str1[0:-2])

#string iteration
for char in str:
    print(char)

#string immutability
str1='C' + str1[1:]
print(str1)

#replace method
str=str.replace("wassup","how are you")
print(str)

#strip()
str2="  i love india  "
print(str2)
print(str2.strip())

#cocatenation
s1="hello"
s2="world"
s3=s1 + " " +s2
print(s3)  #print(s1 +" " + s2)
print(s1*3) #repeating the string

#formatting the string
name="gaurav"
age=19
print(f"Name:{name},Age:{age}")
print("My name is {} and i am {} years old.".format("gaurav",19))

#printing mutiple items
a=[2] *5
print(a)

#extend()
b=[7,4,5]
b.extend([6,12,45])
print(b)