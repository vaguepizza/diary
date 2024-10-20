import datetime
import os

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char
    return result


def write_entry():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = input("Write your diary entry: ")
    mood = input("Rate your mood (happy/neutral/sad): ")
    
    encrypted_entry = caesar_cipher(entry, 3, 'encrypt')
    with open("diary_entries.txt", "a") as file:
        file.write(f"{date}|{mood}|{encrypted_entry}\n")

    print("Entry saved successfully!")


def view_entries():
    if not os.path.exists("diary_entries.txt"):
        print("No entries found.")
        return

    password = input("Enter your password to view entries: ")
    if password != PASSWORD:
        print("Incorrect password. Access denied.")
        return

    print("\nYour Diary Entries:")
    with open("diary_entries.txt", "r") as file:
        for line in file:
            date, mood, encrypted_entry = line.strip().split("|")
            decrypted_entry = caesar_cipher(encrypted_entry, 3, 'decrypt')
            print(f"\nDate: {date}")
            print(f"Mood: {mood}")
            print(f"Entry: {decrypted_entry}")


def set_password():
    global PASSWORD
    PASSWORD = input("Set a password for your diary: ")
    print("Password set successfully!")


while True:
    print("\n--- Encrypted Digital Diary ---")
    print("1. Write a new entry")
    print("2. View past entries")
    print("3. Set password")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        write_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        set_password()
    elif choice == "4":
        print("Thank you for using the Encrypted Digital Diary!")
        break
    else:
        print("Invalid choice. Please try again.")
