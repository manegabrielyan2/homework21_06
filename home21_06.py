#number 1 factorial
"""
def factorial(n : int):
    facto = 1
    while n > 0 :
        facto *= n
        n -= 1
    if n == 0 :
        pass
    return facto 
while True :
    try :
        n = int(input("Please , enter a positive number!"))
        m = factorial(n)
        print(m)
        break
    except Exception :
        print("Type error occured.")
        continue
        """
#number 2 primes
"""
def is_prime(n : int) :
    count = 0
    for i in range(1 , n // 2 + 1) :
        if n % i == 0 :
            count += 1
    if count > 1 :
        return 0
    else :
        return 1
def prime_count() :
    for i in range(1 , 101):
        if is_prime(i) == 1:
            print(i)
prime_count()
    """
#number 3 password 
"""
def ask_pass() :
    password = "hello1234"
    x = input("Enter a password.")
    print("Password matched" if x == password else "Password not matching.")
ask_pass()
    """
#number 4 pattern

"""
def print_pattern():
    matrix =[]
    n = int(input("Please, enter a positive number!"))
    for i in range( 1 , n + 1 ):
        row = [k for k in range(1 , n + 1)]
        matrix.append(row)
    for i in range (0 , n ):
        row = []
        for j in range(0 , n ):
            if i >= j:
                row.append(matrix[i][j])
            matrix.append(row)
    
        print(*row)            
print_pattern()
"""

#number 5 common elements
"""
def find_common_elements(lst1 : list , lst2 : list):
    res = []
    for i in lst1:
        if i in lst2:
            res.append(i)
            lst2.remove(i)
    return res
            
    

lst1 = [1 , 2 , 2 , 3 , 4]
lst2 = [1 ,2 , 5, 'h' , 8]
result = find_common_elements(lst1 , lst2)
print(result)
"""
#number 6 prime factors
"""
def find_prime(k : int):
    count = 0
    for i in range (1 , k // 2 + 1):
        if k % i == 0:
            count += 1
    if count > 1:
        return 0
    else:
        return 1

def find_prime_factors(n : int):
    primes = []
    for i in range(2 , n // 2):
        if n % i == 0 and find_prime(i) == 1:
            primes.append(i)
    return primes
    
n = int(input("Please, enter a positive number!"))
answer = find_prime_factors(n)
print(answer)
"""

# number 7 calculator
"""
def calculator(a , b , operator):
    if operator == '+' :
        return a + b
    elif operator == '-' :
        return a - b 
    elif operator == '*' :
        return a * b
    elif operator == '/' :
        try :
            return  a / b
        except ZeroDivisionError :
            print( "Division by zero not allowed.")   


i = 'hello'
j = 0

while True :
    try :
        while j != 'no' :
            i = input("Do you want to use the calculator?")
            j = i.lower()
            if j == 'no':
                print("See you soon.")
                break
            a = int(input("Please , enter first number."))
            b = int(input("Please , enter second number."))
            operator = input("Enter the operator (+ - / *)")
            c = calculator( a , b , operator)
            print(c)  

            
    except Exception :
        print("Type error.")
        break
        """
#ls = ['apple' , 'banana' , 'grapes' , 'pear']
#counter_list = list(enumerate(ls , 0))
#print(counter_list)


    

