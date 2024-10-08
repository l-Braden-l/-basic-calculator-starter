#Braden Leach,Matthew hall
#Oct 8th 2024
#basic calculator

print('''Hello, welcome to my Basic Calculator!
This script will pronpt you to enter two numbers
And then add, subtract, multiply, or divide the numbers 
depending on the menu option you select.
       ''')
print()
print('''Choose a math operation to perform:
    1. Addition (+)
    2. Subtraction (-)
    3. multiplication (*)
    4. Division (/)
       ''')
math = int(input('Enter your choice (1-4):'))
number_1=float(input('please enter your first number:'))
number_2=float(input('please enter your second number:'))


if math == 1:
   sum = number_1 + number_2 
   print(f'{number_1} plus {number_2} equals: {sum}')
elif math == 2:
   dif = number_1 - number_2 
   print(f'{number_1} minus {number_2} equals: {dif}')
elif math == 3:
   product = number_1 * number_2 
   print(f'{number_1} multiplied by {number_2} equals: {product}')
elif math == 4:
   quotient = number_1 / number_2 
   print(f'{number_1} divided by {number_2} equals: {quotient}')
else:
    print("Invalid input. Please enter a number between 1 and 4.")