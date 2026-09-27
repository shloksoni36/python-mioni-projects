def main():
    print("=== Simple Calculator ===")

try:
        first = float(input("Pehla number: "))
        operator = input("Operation (+, -, *, /): ").strip()
        second = float(input("Dusra number: "))
    except ValueError:
        print("Error: Valid number enter karo.")
        return

if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("Error: Zero se divide nahi kar sakte.")
            return
        result = first / second
    else:
        print("Error: Sirf +, -, *, / allowed hain.")
        return

print(f"Result: {result}")

if __name__ == "__main__":
    main()
# python-mioni-projects
