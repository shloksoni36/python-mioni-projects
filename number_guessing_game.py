import random

def main():
    secret_number = random.randint(1, 100)
    attempts = 0

print("=== Number Guessing Game ===")
    print("1 se 100 ke beech number guess karo.")
    print("Game band karne ke liye q likho.")

while True:
        user_input = input("Tumhara guess: ").strip()

if user_input.lower() == "q":
            print(f"Sahi number tha: {secret_number}")
            break

try:
            guess = int(user_input)
        except ValueError:
            print("Ek valid integer enter karo.")
            continue

if not 1 <= guess <= 100:
            print("Number 1 se 100 ke beech hona chahiye.")
            continue

attempts += 1

if guess < secret_number:
            print("Thoda bada number try karo!")
        elif guess > secret_number:
            print("Thoda chhota number try karo!")
        else:
            print(f"Sahi jawab! Tumne {attempts} attempts liye.")
            break

if __name__ == "__main__":
    main()
