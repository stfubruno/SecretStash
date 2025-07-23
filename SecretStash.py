import json
import os

fileName = 'secret.json'
data = []

try:
    with open(fileName, 'r') as file:
            data = json.load(file)
            print(f'Successfully loaded {fileName}! 🎉')
except FileNotFoundError:
    print(f'Failed to load {fileName} because the file does not exist. 😥')

while True:
    print('--- Dashboard ---')
    print('1 -> Read JSON file')
    print('2 -> Write to JSON file')
    print('3 -> Exit')
    print ('** -> Deletes JSON file')

    procedure = input('Enter your choice: ')

    if procedure == '1':
        print("\n--- Your Secrets ---")
        if not data:
            print('No secrets found!')
        else:
            for secret in data:
                print(f"{secret['callback']} - {secret['string']}")
        print("--------------------\n")

    elif procedure == '2':
        callback = input('Enter a callback: ')
        value = input('Enter the value: ')

        new_data = {
            'id': len(data) + 1,
            'callback': callback,
            'string': value
        }

        data.append(new_data)

        with open(fileName, 'w') as f:
            json.dump(data, f, indent=4)

        print(' ')
        print("\nNew secret added successfully! ✨\n")
        print(' ')

    elif procedure == '**':
        print(' ')
        try:
            os.remove(fileName)
            print(f'Successfully deleted {fileName}!')
        except FileNotFoundError:
            print(f'Failed to remove {fileName}!')
        print(' ')

    elif procedure == '3':
        print('Exiting program. Goodbye! 👋')
        break

    else:
        print(' ')
        print('Invalid choice. Please try again...')
        print(' ')
