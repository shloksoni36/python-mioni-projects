def main():
    print("=== Multiplication Table ===")

try:
        number = int(input("Kis number ka table chahiye? "))
        limit = int(input("Kahan tak? Jaise 10 ya 20: "))
    except ValueError:
        print("Error: Valid integers enter karo.")
        return

if limit <= 0:
        print("Error: Limit zero se badi honi chahiye.")
        return

print(f"\n{number} ka table:")

for multiplier in range(1, limit + 1):
        print(f"{number} x {multiplier} = {number * multiplier}")

if __name__ == "__main__":
    main()
