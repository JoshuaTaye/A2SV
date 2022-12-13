# FizzBuzz
def fizzbuzz(n):
    lst=[]
    for i in range(n+1):
        if i%3==0 and i%5!=0 and i>0:
            lst.append('Fizz')
        elif i%5==0 and i%3!=0 and i>0:
            lst.append('Buzz')
        elif i%3==0 and i%5==0 and i>0:
            lst.append('FizzBuzz')  
        elif i>0:
            lst.append(str(i))
    return(lst)
n=int(input('Enter No.:'))
print(fizzbuzz(n))  
