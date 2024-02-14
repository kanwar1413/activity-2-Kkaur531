#1. (10 points) Write a Python function `getPrimeNumbers(n)` which returns a list containing all 
#prime numbers between 2 and _n_.  Create a helper function to determine if a particular number is
#prime and then use a comprehension to generate your list.
def getPrimeNumbers(n):
    prime=[2,3,5,7]
    for i in range(2,n+1):
        if((i%2!=0)&(i%3!=0)&(i%5!=0)&(i%7!=0)):
            prime.append(i)
        i+=1
    return prime
print(getPrimeNumbers(21))
