while True:
    try:
        user_loss_input = input("Have you lost money this year? (type yes or no): ").strip().lower()

        if user_loss_input == "yes":
            print("We are sad to hear you lost money.")
            Pv = float(input("Please insert your initial investment: "))
            r = float(input("Please insert the rate of depreciation (in percentage): "))
            n = float(input("Please insert the number of years you had invested for: "))

            FVL = Pv * (1 - (r / 100)) ** n

            print("Money lost:" + FVL)

        elif user_loss_input == "no":
            print("Congratulations! We will need some information to calculate your compound interest.")
            cv = float(input("Please insert your initial investment: "))
            i = float(input("Please insert the rate of appreciation (in percentage): "))
            ny = float(input("Please insert the number of years you had invested for: "))
            cp = float(input("Please insert the number of compounding periods per year: "))

            FV = cv * (1 + (i / (100 * cp))) ** (cp * ny)

            print("Money gained: " + FV)

        else:
            print("Invalid input, please type 'yes' or 'no'.")
            continue

        break

    except EOFError:
        break
    except ValueError:
        print("Invalid input, please enter numeric values where required.")


     
    
    
                   

   
       
