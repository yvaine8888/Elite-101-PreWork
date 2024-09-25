print('Welcome to the Elite 101 Chatbot!')
user_name = input('What is your name?: ')
print('Nice to meet you, ' + user_name + '!')
age = input('How old are you?: ')
age = int(age)

if age < 15:
    print(f'Oh, to be {age} again.')
elif age < 18:
    print(f"You're {age}? Good luck.") 
elif age < 55:
    print(f"You're {age}? Wow...")
elif age < 120:
    print(f"You're {age}? Wow, you're old.")
elif age >= 120:
    print(f"You're {age}? Now you are lying.")
else:
    print(f"{age} would not work. You didn't need to lie")
print()
print('What can I do for you today?')
print()

while True:
    print('--------------------------------------------')
    print('Please choose from the following options:')
    print('1. Option1')
    print('2. Option2')
    print('3. Option3')
    print('4. Exit the conversation.')
    user_choice = input('Please choose a number 1-4: ')
    print()
    if user_choice == '1':
        print('Option1')
    elif user_choice == '2':
        print('Option2')
    elif user_choice == '3':
        print('Option3')
    elif user_choice == '4':
        print('Goodbye ' + user_name + '! Have a nice day.')
        break;
    else:
        print('Invalid input.')
