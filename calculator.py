def bisaya_calculator():

    while True:
        print('welcome sa bisaya na calculator')

        try:
            num1 = float(input("butangi og isa  na number: "))
            operator = input("butngi og operator (+, -, *, /): ")
            num2 = float(input("butangi og ika duha na number: "))


        except ValueError:
            print('bugo man siguro ka butangi daw og tama na numebers salamat ')
            continue


        if operator == '+':
           result =  num1 + num2

        elif operator == '-':
            result = num1 - num2

        elif operator == '*':
            result  = num1 * num2

        elif operator == '/':
            num1 = num1 / num2
            if num2 == 0:
                result = "bugo man ata ka (dli mana ma devide sa zero)"
            else:
                result = num1 / num2
        else:
            result = "bulok maning yawaa ni"

        print(f"Result: {result}")

        quit_choice = input("gusto paka mag corrupt? (y/n): ").lower()
        if quit_choice != 'y':
            print("wais ang saket(gusto pako mo utro?)")
            break

bisaya_calculator()











