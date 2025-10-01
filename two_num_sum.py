# num1=20
# num2=30
# result=num1+num2
# print("The sum is:",result)

# num1=float(input('Enter first number: '))
# num2=float(input('Enter second number: '))
# print(num1+num2)

def get_number():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
num1=get_number()
num2=get_number()
print("The sum is:",num1+num2)

