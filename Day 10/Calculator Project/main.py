import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply (n1 , n2):
    return n1 * n2

def divide (n1 , n2):
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
#print(operations["*"](4 , 3))
def calculate():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("what is your first number:"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("what is your operation:")
        num2 = float(input("what the next number:"))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} + {num2} = {answer}")

        choice = input("would you like to continue? (y/n)")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculate()
calculate()








