def numgen():
    from phone_gen import PhoneNumber
    import time, os, platform
    st = time.time()
    try:
        numbers = []
        def num_gen(country, quantity):
            number = PhoneNumber(country)    
            phone_number = 0
            ostype = platform.system()
            print("Generating numbers...")
            for i in range(quantity):
                phone_number = number.get_number()
                if phone_number not in numbers:
                    numbers.append(phone_number)
                else:
                    phone_number = number.get_number()
                    numbers.append(phone_number)       
            with open ("numbers.txt",'w') as file:
                for i in numbers:
                    print(f'Sending {i} to outputfile...')
                    time.sleep(0.001)
                    if ostype == 'Linux':
                        os.system('clear')
                    elif ostype == 'Windows':
                        os.system('cls')
                    else:
                        pass      
                    file.write(i + "\n")
                file.close()
        try:
            country = input("Enter the full name of the country you want to generate numbers for:\n").title()
        except Exception as e:  
            print(f"Please Enter the correct country name\nHint: {e}")
            exit()
        quantity = int(input("How many numbers do you want?:\n"))
        num_gen(country, quantity)
        et  = time.time()
        tt = round(et - st, 2)
        print(f"{len(numbers)} Number(s) generated and saved successfully in {tt}secs")
    except Exception as e:
        print(f"A fatal error occured {e}\nRecheck your inputs!!!!!!!")
        exit() 
    return "numbers.txt"       