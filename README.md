# Encrypted Digital Diary with Mood Tracking

This is a simple Python-based **Encrypted Digital Diary** that allows users to write, encrypt, and store diary entries along with mood tracking. The diary entries are encrypted using a Caesar Cipher, and users must provide a password to decrypt and view their entries. The project demonstrates basic file I/O operations, encryption, and password protection.

## Features

- **Write a diary entry**: Users can write a diary entry and rate their mood (happy, neutral, sad). The entry is encrypted before being saved.
- **Mood tracking**: Each entry includes a mood rating (happy, neutral, sad) for the user to track their emotional state over time.
- **Encryption**: Entries are encrypted using a simple Caesar Cipher to ensure privacy.
- **Password protection**: Users can set a password for the diary, which is required to decrypt and view the entries.
- **View past entries**: Users can view their previous diary entries after entering the correct password.
- **File-based storage**: Entries are saved in a text file, ensuring that they persist between sessions.

## How It Works

1. **Encryption**: The diary entries are encrypted using a Caesar Cipher, which shifts each letter by 3 positions in the alphabet.
2. **File Storage**: Entries are stored in a text file (`diary_entries.txt`) in the format:
   ```
   date|mood|encrypted_entry
   ```
3. **Password Protection**: A global password must be set, and users need to provide this password to view their entries.

## Requirements

- **Python 3.x** installed on your system.

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vaguepizza/encrypted-diary.git
   cd encrypted-diary
   ```

2. **Run the script**:
   ```bash
   python diary.py
   ```

3. **Menu Options**:
   - **1**: Write a new diary entry (with mood tracking).
   - **2**: View past entries (requires password).
   - **3**: Set a password for your diary.
   - **4**: Exit the program.

## Project Structure

```
├── diary.py            # Main Python script
├── diary_entries.txt   # File where encrypted entries are stored (created after first entry)
└── README.md           # Project documentation
```

## Usage Instructions

1. **Set a Password**:
   - Before writing entries, you need to set a password for your diary. Use option 3 in the menu to set it.
   
2. **Write an Entry**:
   - Choose option 1 to write a new diary entry. After entering your text and mood, the entry will be encrypted and saved in the file.

3. **View Entries**:
   - Choose option 2 to view your past entries. You'll be prompted for the password, and upon correct entry, the diary entries will be decrypted and displayed.

4. **Exit**:
   - Option 4 will exit the program.

## Example

```plaintext
--- Encrypted Digital Diary ---
1. Write a new entry
2. View past entries
3. Set password
4. Exit
Enter your choice (1-4): 1
Write your diary entry: Had a great day learning Python!
Rate your mood (happy/neutral/sad): happy
Entry saved successfully!

--- Encrypted Digital Diary ---
1. Write a new entry
2. View past entries
3. Set password
4. Exit
Enter your choice (1-4): 2
Enter your password to view entries: ****
Date: 2024-10-19 14:00:00
Mood: happy
Entry: Had a great day learning Python!
```

## Limitations and Future Enhancements

- **Simple encryption**: Currently, a basic Caesar Cipher is used. In the future, this could be replaced with more secure encryption methods.
- **Password storage**: The password is not stored persistently, so it needs to be re-entered every time you run the program. A persistent password mechanism could be implemented.
- **Enhanced mood analysis**: A more detailed analysis of mood trends could be added for users to track emotional well-being over time.

## Contributing

Feel free to fork this project, submit pull requests, or suggest improvements!