import math

def main():
    print("=== Temperature Converter ===")
    print("1: Celsius se Fahrenheit")
    print("2: Fahrenheit se Celsius")

choice = input("Option 1 ya 2 chuno: ").strip()

if choice not in ("1", "2"):
        print("Error: Sirf 1 ya 2 choose karo.")
        return

try:
        temperature = float(input("Temperature enter karo: "))
    except ValueError:
        print("Error: Valid number enter karo.")
        return

if not math.isfinite(temperature):
        print("Error: Temperature finite number hona chahiye.")
        return

if choice == "1":
        if temperature < -273.15:
            print("Error: Absolute zero se neeche temperature hai.")
            return

result = temperature * 9 / 5 + 32
        print(f"{temperature} °C = {result:.2f} °F")
    else:
        if temperature < -459.67:
            print("Error: Absolute zero se neeche temperature hai.")
            return

result = (temperature - 32) * 5 / 9
        print(f"{temperature} °F = {result:.2f} °C")

if __name__ == "__main__":
    main()
