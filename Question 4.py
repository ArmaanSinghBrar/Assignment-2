#Finding the greatest of three numbers entered
number1 = float(input("Enter the first number ="))
number2 = float(input("Enter the second number ="))
number3 = float(input("Enter the thirds number ="))
if(number1>number2 and number1>number3):              #We can either make cases to find the greatest number or use max
    print("The first number is the greatest")
elif(number2>number1 and number2>number3):
    print("The second number is the greatest")
elif(number3>number1 and number3>number2):
    print("The third number is the greatest")
else:
    print("ALl the numbers are equal")
print("The value of the greatest number is:",max(number1,number2,number3))
