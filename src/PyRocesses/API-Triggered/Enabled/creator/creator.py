# test.py
try:
    print('Executing creator.py...')
    with open('testcase.txt', 'w') as f:
        f.write('This is a test.')
    print('test.txt created successfully.')
except Exception as e:
    print(f'Failed to create test.txt: {e}')