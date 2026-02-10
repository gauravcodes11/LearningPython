#even or odd
num=int(input("enter a number:"))
if num%2:
    print("the number is odd")
else:
    print("the number is even")
#positive, negative or zero
num=int(input("Enter a number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")
#decide a number is positive even, positve odd, negative even, negative odd or zero
num=int(input("enter a number:"))
if num>0:
    res="postive odd" if num%2 else "positve even"
    print(res)
elif num<0:
    res1="negative odd" if num%2 else "negative even"
    print(res1)
else:
    print("zero")
#take two numbers and tell which is greater or if they are same
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if a==b:
    print("both numbers are equal")
elif a>b:
    print("a is greater")
else:
    print("b is greater")
#Check if user is eligible to vote
num=int(input("enter your age:"))
if num>=18:
    print("you are eligible to vote")
#Check if a number is positive     
num=int(input("enter a number:"))
if num>0: print("positive number")
#Check if a student is pass/fail in exam.
marks=int(input("enter your marks:"))
res="pass" if marks>40 else "fail"
print(res)
#Check if a user has balance to buy an item
balance=float(input("enter your account balance:"))
item_price=float(input("enter the item price:"))
if balance>item_price:
    print("you can purchase the item")
else:
    print("insufficient balance")
#Suggest a mode of transport based on distance
distance=int(input("enter the diatance:(in km)"))
if distance<=2:
    print("you can walk")
elif distance<=5:
    print("you can use bicycle")
elif distance<50:
    print("take a car or public transport")
else:
    print("take train or flight")
#Battery status
battery=int(input("enter your battery percentage:"))
if battery>80:
    print("battery is full")
elif battery>35:
    print("battery is half")
else:
    print("battery is low")
#Login with username and password
username=input("enter the username:")
password=input("enter your password:")
if username=="abcd":
    if password=="1234":
        print("login successful")
    else:
        print("incorrect password")
else:
    print("username not found")
#Check exam pass and scholarship eligibility
marks=int(input("enter your marks:"))
if marks>50:
    if marks>80:
        print("passesd with scholarship")
    else:
        print("passed without scholarship")
else:
    print("failed")
#Check if number is even using Ternary statement
num=int(input("enter your number:"))
res="odd" if num%2 else "even"
print(res)
#Compare two numbers using Ternary statement
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("a is greater" if a>b else "b is greater")
#Temperature check using Ternary statement
temp=float(input("enter the current temperature(in celsius):"))
print("hot" if temp>=30 else "cool")
#Assign grade
grade=input("enter your grade(A/B/C..):").upper()
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("need to try harder")
#Activity Suggestion based on weather condition
weather=(input("enter the current weather conditon(rainy/cloudy/snowy/sunny):")).lower()
match weather:
    case "sunny":
        print("go for a picnic")
    case "rainy":
        print("stay inside")
    case "cloudy":
        print("drink some tea and enjoy your favourite show")
    case "snowy":
        print("exercise caution while travelling")
    case _:
        print("unknown input")
#Mobile notification settings based on user profile mode
mode=input("what mode is in your mobile(silent/normal/vibrate/dnd):").lower()
match mode:
    case "silent":
        print("call notifications and message notification will be muted")
    case "normal":
        print("the notification will make a sound")
    case "vibrate":
        print("it will vigrate upon call and mesaages")
    case "dnd":
        print("no sound will be heard")