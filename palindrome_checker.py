def is_palindrome(text):
    cleaned = "".join(
        character for character in text.casefold()
        if character.isalnum()
    )

if not cleaned:
        raise ValueError("Kam se kam ek letter ya number likho.")

return cleaned == cleaned[::-1]

def main():
    print("=== Palindrome Checker ===")
    text = input("Koi word, sentence ya number likho: ")

try:
        if is_palindrome(text):
            print("Haan! Ye palindrome hai.")
        else:
            print("Nahi, ye palindrome nahi hai.")
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
