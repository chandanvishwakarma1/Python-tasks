print("\n----------------Basic Arithmetic Operation-------------------")
print("Enter he values for two number below: ")
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))

result = (num1 + num2)
print(f"Addition of {int(num1) if num1.is_integer() else num1} and {int(num2) if num2.is_integer() else num2} is {int(result) if result.is_integer() else result}")

    
result = (num1 - num2)
print(f"Subtraction of {int(num2) if num2.is_integer() else num2} from {int(num1) if num1.is_integer() else num1  } is {int(result) if result.is_integer() else result}")


result = (num1 * num2)
print(f"Multiplication of {int(num1) if num1.is_integer() else num1} and {int(num2) if num2.is_integer() else num2} is {int(result) if result.is_integer() else result}")

if num2 != 0:
        result = num1 / num2
        print(f"Division of {int(num1) if num1.is_integer() else num1} by {int(num2) if num2.is_integer() else num2} is: {int(result) if result.is_integer() else result}")
else:
        print("Division by zero is not allowed.")



