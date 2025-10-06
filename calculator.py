def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero not possible"
    return a / b

def mod(a, b):
    if b == 0:
        return "Modulus by zero not possible"
    return a % b

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

try:
    ch = input("Enter choice (1/2/3/4/5): ")

    if ch not in ('1', '2', '3', '4', '5'):
        print("Invalid choice")
    else:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if ch == '1':
            print(f"{n1} + {n2} = {add(n1, n2)}")
        elif ch == '2':
            print(f"{n1} - {n2} = {sub(n1, n2)}")
        elif ch == '3':
            print(f"{n1} * {n2} = {mul(n1, n2)}")
        elif ch == '4':
            result = div(n1, n2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{n1} / {n2} = {result:.2f}")
        else:
            result = mod(n1, n2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{n1} % {n2} = {result}")

except ValueError:
    print("Enter valid numbers")
except Exception as e:
    print("Error:", e)
