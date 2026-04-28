bot_name: str = 'waynegpt'
print(f'Hello {bot_name}! Unsa akong himoon para sa imoha dawg?')

while True:
    user_input = input('You: ').lower()

    if user_input in ['wassap dawg', 'hi', 'hello']:
        print('wassap daw how are u?')

    elif user_input == 'bye':
        print('babye dawg')
        break  #

    elif user_input == 'naakoy gusto pangutana dawg':
        print("what the hell is it?")

    elif user_input == 'kamusta dawg?':
        print('im very fine, im very okay')

    elif user_input == 'lamat dawg':
        print('no problems dawg')

    elif user_input in ['+', 'add']:
        print(f'{bot_name}: put numbers my guy')
        try:

            num1 = float(input('First number: '))
            num2 = float(input('Second number: '))
            print(f'Result = {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: u dumb ass wrong number')

    elif user_input in ['-', 'subtract', 'minus']:
        print(f'{bot_name}: put numbers my guy')
        try:
            num1 = float(input('First number: '))
            num2 = float(input('Second number: '))
            print(f'Result = {num1 - num2}')
        except ValueError:
            print(f'{bot_name}: u dumb ass wrong number')

    elif user_input in ['*', 'multiply', 'times']:
        print(f'{bot_name}: put numbers my guy')
        try:
            num1 = float(input('First number: '))
            num2 = float(input('Second number: '))
            print(f'Result = {num1 * num2}')
        except ValueError:
            print(f'{bot_name}: u dumb ass wrong number')
    elif user_input in ['/', 'divide']:
        print(f'{bot_name}: put numbers my guy')
        try:
            num1=float(input('First number: '))
            num2 = float(input('Second number: '))
            print(f'Result = {num1 / num2}')
        except ValueError:
            print(f'{bot_name}: u dumb ass wrong number')

    else:
        # This catches anything that doesn't match the commands above
        print(f'{bot_name}: cant understand dawg repeat it again')