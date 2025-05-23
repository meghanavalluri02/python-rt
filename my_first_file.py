try:
    with open('my_first_file.txt', 'w') as file:
        file.write('Hello, kirthik')
        print('File written successfully.')
except Exception as e:
    print(f'An error occurred: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
