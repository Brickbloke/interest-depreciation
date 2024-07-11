while True:
  try:
    user_loss_input = input("have you lost money this year? (type = yes or no)")
    user_loss_input =
    if user_loss_input == "yes"
        print(" we are sad to hear you lost money ") 
        Pv = input("numbers insert your intial investment") #intitial cash investment
        Pv = float(Pv)
        r = input("insert the rate of depreciation") #disinterst rate
        r = float(r)
        n = input("please insert the number of year you had invested for") #years
        n = float(n)

        FVL = Pv * (1 - ( r / 100 ) ** n
                    
    elif user_loss_input == "no":
        print("congragulations we will need some information to calculate your compound interest")
        cv = input("numbers insert your intial investment") #initial cash investment
        cv = float(cv)
        i = input("insert the rate of appreciation") #interst rate
        i = float(i)
        ny = input("please insert the number of year you had invested for") #years
        ny = float(ny)
        cp = input("compounding periods for your investment") #compounding times
        cp = float(cp)
    
        FV = cv * (1 + ( i / ( 100 * cp ) ) ** ( cp * ny )
        
    else:
        continue
    

   
       
