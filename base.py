
'''
program that first reads two pairs of integers from standard input. 
Each pair contains a base (from 2 to 10) and a number written in that base.

Next, read an integer indicating the base in you should print the sum, difference, product and integer quotient of these two numbers, with each of these values on a separate line.

The numbers' values (but not necessarily their written representations, e.g. in binary!) will fit into a two-byte integer.

Example:

Input:
5 11 2 101 7

Output:

14
1
42
1
'''


a = list(map(int, input().split()))
system_1 = a[0]
number_1 = a[1]
system_2 = a[2]
number_2 = a[3]
x = a[4]


def to_10(number,system):
    number=str(number)
    a = []
    for i in range(len(number)):
        a.append(int(number[i]))
    hodnota = 0
    n = len(a) 
    for i in range(len(a)):
        n -= 1
        hodnota += a[i]*(system**n)
    return(hodnota)

number_1 = to_10(number_1,system_1)  
number_2 = to_10(number_2,system_2)   

summ = number_1 + number_2 
diffetence =number_1 - number_2
product = number_1 * number_2
quotient =number_1 // number_2

  
def to_x(number,system):
    arr = []
    q = ''
    
    if system == 10:
        return(number)
    else: 
        while number != 0:
            arr.append(number % system)
            number = number // system
        for i in range(len(arr)-1,-1,-1):
            q += str(arr[i])
        return(int(q))
    
print(to_x(summ,x))
print(to_x(diffetence,x))
print(to_x(product,x))
print(to_x(quotient,x))
 

  
    