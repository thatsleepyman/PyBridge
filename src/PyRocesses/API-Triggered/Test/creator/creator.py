import sys


def process_message(message):
    try:
        print('Executing creator.py...')
        with open('creator_test.txt', 'w') as f:
            f.write(message)  # Write the sanitized message to the file
        print('creator_test.txt created successfully.')
    except Exception as e:
        print(f'Failed to create creator.txt: {e}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        message = sys.argv[1]  # Get the sanitized message from the command line arguments
        process_message(message)
    else:
        print('No message received.')
