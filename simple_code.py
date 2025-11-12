# Simple Math Functions
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

'''
def power(a,b):
   return a ** b
'''

if __name__ == "__main__":
    print("Addition of 5 and 7 is: ", add(5,7))
    print("Subctraction of 5 from 10 is: ", subtract(10,5))
    print("Multiplication of 7 and 8 is: ", multiply(7,8))
    print("Divison of 100 by 25 is: ", divide(100,25))
    #print("2 to the power of 7 is: ", power(2,7))
