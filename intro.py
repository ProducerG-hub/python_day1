num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1/num2

print("1.Addition\n" "2.Substraction\n" "3.Multiplication\n" "4.division")
choose = int(input("Choose the operation: "))

if choose==1:
    print("Result:",add)
if choose==2:
    print("Result:",sub)
if choose==3:
    print("Result:",multi)
if choose==4:
    print("Result:",div)