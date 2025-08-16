print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("Choose an operation; "))
if (option in [1, 2, 3, 4]):
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter Second number: "))
    if (option == 1):
        Result = first_number + second_number
    elif (option == 2):
        Result = first_number - second_number
    elif (option == 3):
        Result = first_number * second_number
    elif (option == 4):
        Result = first_number // second_number
else:
    print("You entered an invalid Number")

print("The result of the operation is {}".format(Result))
