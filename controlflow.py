#factorial
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)

#factorial- another way
n = int(input())
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

#type of pattern
n = int(input())
for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " "*(n-2) + "*")

#more practise on coding platforms 
#also revised older codes