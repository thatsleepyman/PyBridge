import sys
import os

def process_message(message):
    try:
        # Save the message to a text file
        with open("./message2.txt", "w") as file:
            file.write(message)
        print("Message saved to message.txt")
        return "File created successfully"
    except Exception as e:
        print("Error:", e)
        return "Failed to create file"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        message = sys.argv[1]
        response = process_message(message)
        print(response)  # Return response to be captured by request.py
    else:
        print("No message received.")
