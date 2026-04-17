try:
    # Ask the user to enter a short note/message.
    note = input("Enter a short note: ")

    with open("notes.txt", "w") as file:
        file.write(note + "\n")

    print("\nNote saved successfully!")

    # 2. Read and display
    with open("notes.txt", "r") as file:
        content = file.read()
        print("\nContent of file: ")
        print(content)

    # 3. Append new Data.

    new_note = input("Enter another note: ")

    with open("notes.txt", "a") as file:
        file.write(new_note + "\n")

    print("\nNote added successfully!")

    # Display updated content
    with open("notes.txt", "r") as file:
        updated = file.read()
        print("\nUpdated content: ")
        print(updated)

# Error Handling
except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("An error occurred: ", e)