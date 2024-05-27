# test.py
try:
    print('Executing creator.py...')
    with open('test.txt', 'w') as f:
        f.write('This is a test.')
    print('test.txt created successfully.')
except Exception as e:
    print(f'Failed to create test.txt: {e}')