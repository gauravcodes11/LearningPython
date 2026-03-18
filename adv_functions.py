#recursion--factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#fibonacci sequence
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))

#types of recursion
def tail_fact(n, acc=1):
    # Base case
    if n == 0:
        return acc
    # Tail recursive call with an accumulator
    else:
        return tail_fact(n-1, acc * n)

def nontail_fact(n):
    # Base case
    if n == 1:
        return 1
    # Non-tail recursive call because the multiplication happens after the call
    else:
        return n * nontail_fact(n-1)

    # Example usage
print(tail_fact(5))  
print(nontail_fact(5))

#map() function
s=['1','2','3','4']
res=map(int,s) #res is a map object, map is a function
print(list(res))
    #extracting first character from strings
words=['apple','banana',"cherry"]
res=map(lambda s:s[0],words)
print(list(res))

#filter() function
def starts_a(w):
    return w.startswith("a")
li=["apple","banana","apricot","cherry","avocado"]
res=filter(starts_a,li)
print(list(res))
    #another example
def even(n):
    return n%2==0
li=[1,2,6,4,5,8]
res=filter(even,li)
print(list(res))
    #another example  
li=["apple","banana","apricot","cherry","avocado"]
a=filter(lambda x:len(x)>5,li)
print(list(a))

#reduce() function
from functools import reduce
a=["I","love", "cricket"]
r=reduce(lambda x,y:x+" "+y,a)
print(r)

#accumulate() function
from itertools import accumulate
from operator import add

a = [1, 2, 3, 4, 5]
res = accumulate(a, add)
print(list(res))
