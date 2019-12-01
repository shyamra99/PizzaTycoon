import random
import time
# Display Game Opening

# Create GUI for game's initial opening screen ****

print ("                       *****************************************")
print ("                       *                                       *")
print ("                       *    PIZZA TYCOON - COMMAND-LINE VER.   *")
print ("                       *                                       *")
print ("                       *****************************************\n")

print ("The objective of the game is to achieve $10,000 and have your Store in the Mall \n")

# Enter in player information and reiterate it to the player
store_name = input("Enter the Name of your store: ")
player_name = input("Enter your Character Name: ")
print(player_name + ", you are now the owner of " + store_name + ". Now turn yourself into a Pizza Tycoon!")

# Set the initial cash balance of the player to $100
cash_balance = float(100)
#Set initial menu option to 0 so that the game can run initially
main_menu_option = 0
#Set the initial inventory of all ingredients to 0
cheese_inventory = 0
tomatoes_inventory = 0
olives_inventory = 0
mushrooms_inventory = 0
#Set the index of your location to 0; i.e. do not have
UTSC_index = 0
Conv_index = 0
Mall_index = 0
location = "backyard"

#The game will continue running as long as the option is not to exit
while main_menu_option != 4:


    # Display the Main Menu to enter an action

    main_menu_option = input("Enter the number of the action you would like to do: \n1 Buy Ingredients \n2 Make your pizza \n3 Upgrade Locations \n4 Exit the Game \n")
    main_menu_option = int(main_menu_option)
    
    # If input that is not 1-4 is selected to buy ingredients, ask to re-enter
       
    if (main_menu_option < 1 or main_menu_option > 4):
            while (main_menu_option < 1 or main_menu_option > 4):  
                    main_menu_option = input ("You must choose an option from 1-4: \n1. Buy Ingredients \n2. Make your pizza \n3. Upgrade Locations \n4. Exit the Game \n")
                    main_menu_option = int(main_menu_option)
                    
    #If option is to exit the game (4), break out of loop and end the game:
    if (main_menu_option != 4):

        #If option 1 is selected, show the ingredients menu
        if (main_menu_option == 1):
            
            ingredient_choice = 0
            while (ingredient_choice != 5):
            
                ingredient_choice= input("Choose the number of the ingredient you want to buy: \n1. Cheese ($1.00 each) \n2. Tomatoes ($1.00 each) \n3. Olives ($1.00 each) \n4. Mushrooms ($2.00 each) \n5. Return to Main Menu \n")
                ingredient_choice = int(ingredient_choice)
                
                # If the choice is not 1-5, we need them to re-enter the choice
                while (ingredient_choice < 1 or ingredient_choice > 5):
                        
                        ingredient_choice = input("You must choose an option from 1-5: \n1. Cheese ($0.50 each) \n2. Tomatoes ($1.00 each) \n3. Olives ($1.00 each) \n4. Mushrooms ($2.00 each) \n5. Return to Main Menu \n")
                        ingredient_choice = int(ingredient_choice)
            
                if (ingredient_choice != 5):
                    
                    if (ingredient_choice == 1):
                        
                        ingredient = "cheese"
                        ingredient_cost = int(1)
                        total_bought = 0
                        purchase_quantity = input("How many " + ingredient + " would you like to purchase? \n")
                        purchase_quantity = int(purchase_quantity)
                            
                        purchase_total = (purchase_quantity*ingredient_cost)
                            
                        if (cash_balance >= purchase_total):
                            
                            cash_balance = cash_balance - purchase_total
                            print("You have purchased " + str(purchase_quantity) + " " + ingredient + "! Your remaining cash balance is " + str(cash_balance))
                                
                            total_bought = total_bought + purchase_quantity
                            
                        else:
                            purchase_continue_exit = ""
                            while (purchase_continue_exit != "exit"):
                                purchase_continue_exit = input("You do not have enough money to purchase " + str(purchase_quantity) + " " + ingredient + "! Enter another amount to purchase or enter 'exit' to go back? \n")
                                    
                                if (purchase_continue_exit != "exit"):
                                    purchase_quantity = int(purchase_continue_exit)
                                    purchase_total = (purchase_quantity*0.5)
                                        
                                    if (cash_balance >= purchase_total):
                                        
                                        cash_balance = cash_balance - purchase_total
                                            
                                        print("You have purchased " + str(purchase_quantity) + " " + ingredient + "! Your remaining cash balance is " + str(cash_balance))
                                            
                                        total_bought = total_bought + purchase_quantity
                                            
                                        purchase_continue_exit = "exit"                                            
                        cheese_inventory = cheese_inventory + total_bought
                        
                        print ("You now have " + str(cheese_inventory) + " cheese in stock")
                                        
                    if (ingredient_choice == 2):
                                            
                        ingredient = "tomatoes"
                        ingredient_cost = int(1)
                        total_bought = 0
                        purchase_quantity = input("How many " + ingredient + " would you like to purchase? \n")
                        purchase_quantity = int(purchase_quantity)
                            
                        purchase_total = (purchase_quantity*ingredient_cost)
                            
                        if (cash_balance >= purchase_total):
                            
                            cash_balance = cash_balance - purchase_total
                            print("You have purchased " + str(purchase_quantity) + " " + ingredient + "! Your remaining cash balance is " + str(cash_balance))
                                
                            total_bought = total_bought + purchase_quantity
                            
                        else:
                            purchase_continue_exit = ""
                            while (purchase_continue_exit != "exit"):
                                purchase_continue_exit = input("You do not have enough money to purchase " + str(purchase_quantity) + " " + ingredient + "! Enter another amount to purchase or enter 'exit' to go back? \n")
                                    
                                if (purchase_continue_exit != "exit"):
                                    purchase_quantity = int(purchase_continue_exit)
                                    purchase_total = (purchase_quantity*0.5)
                                        
                                    if (cash_balance >= purchase_total):
                                        
                                        cash_balance = cash_balance - purchase_total
                                            
                                        print("You have purchased " + str(purchase_quantity) + " " + ingredient + "! Your remaining cash balance is " + str(cash_balance))
                                            
                                        total_bought = total_bought + purchase_quantity
                                            
                                        purchase_continue_exit = "exit"          
                                        
                        tomatoes_inventory = tomatoes_inventory + total_bought
                        print ("You now have " + str(tomatoes_inventory) + " tomatoes in stock")
                    
                    if (ingredient_choice == 3):
                        
                        ingredient = "olives"
                        ingredient_cost = 1
                        total_bought = 0
                        purchase_quantity = input("How many " + ingredient + " would you like to purchase? \n")
                        purchase_quantity = int(purchase_quantity)
                            
                        purchase_total = (purchase_quantity*ingredient_cost)
                            
                        if (cash_balance >= purchase_total):
                            
                            cash_balance = cash_balance - purchase_total
                            print("You have purchased " + str(purchase_quantity) + " " + ingredient + "! Your remaining cash balance is " + str(cash_balance))
                                
                            total_bought = total_bought + purchase_quantity
                            
                        else:
                            purchase_continue_exit = ""
                            while (purchase_continue_exit != "exit"):
                                purchase_continue_exit = input("You do not have enough money to purchase " + str(purchase_quantity) + " " + ingredient + "! Enter another amount to purchase or enter 'exit' to go back? \n")
                                    
                                if (purchase_continue_exit != "exit"):
                                    purchase_quantity = int(purchase_continue_exit)
                                    purchase_total = (purchase_quantity*0.5)
                                        
                                    if (cash_balance >= purchase_total):
                                        
                                        cash_balance = cash_balance - purchase_total
                                            
                                        print("You have purchased " + str(purchase_quantity) + " " + ingredient + "! Your remaining cash balance is " + str(cash_balance))
                                            
                                        total_bought = total_bought + purchase_quantity
                                            
                                        purchase_continue_exit = "exit"                                            
                        olives_inventory = olives_inventory + total_bought
                        
                        print ("You now have " + str(olives_inventory) + " olives in stock")
                        
                    if (ingredient_choice == 4):
                        
                        ingredient = "mushrooms"
                        ingredient_cost = 2
                        total_bought = 0
                        purchase_quantity = input("How many " + ingredient + " would you like to purchase? \n")
                        purchase_quantity = int(purchase_quantity)
                            
                        purchase_total = (purchase_quantity*ingredient_cost)
                            
                        if (cash_balance >= purchase_total):
                            
                            cash_balance = cash_balance - purchase_total
                            print("You have purchased " + str(purchase_quantity) + " " + ingredient + "! Your remaining cash balance is " + str(cash_balance))
                                
                            total_bought = total_bought + purchase_quantity
                            
                        else:
                            purchase_continue_exit = ""
                            while (purchase_continue_exit != "exit"):
                                purchase_continue_exit = input("You do not have enough money to purchase " + str(purchase_quantity) + " " + ingredient + "! Enter another amount to purchase or enter 'exit' to go back? \n")
                                    
                                if (purchase_continue_exit != "exit"):
                                    purchase_quantity = int(purchase_continue_exit)
                                    purchase_total = (purchase_quantity*0.5)
                                        
                                    if (cash_balance >= purchase_total):
                                        
                                        cash_balance = cash_balance - purchase_total
                                            
                                        print("You have purchased " + str(purchase_quantity) + " " + ingredient + "! Your remaining cash balance is " + str(cash_balance))
                                            
                                        total_bought = total_bought + purchase_quantity
                                            
                                        purchase_continue_exit = "exit"                          
                        mushrooms_inventory = mushrooms_inventory + total_bought
                        
                        print ("You now have " + str(mushrooms_inventory) + " mushrooms in stock")
                        
                        
        if (main_menu_option == 2):
            
            if(cheese_inventory == 0 and tomatoes_inventory == 0 and olives_inventory == 0 and mushrooms_inventory == 0 and pineapples_inventory == 0):
                print("You do not have any cheese/tomato/olive/mushroom to make your pizza")
                exit = input("Enter any key to go back to main menu to buy more: ")
            
            else:
        
        
                #providing a chart of the current ingredients
                
                print("                            !===============!")
                print("                            !CURRENT BALANCE!")
                print("                            !===============!")
                print("+----------------+---------------+-------------+----------------+----------+")
                print("|     Cheese     |    Tomatoes   |   Olives    |    Mushrooms   |   Cash   |")
                print("+----------------+---------------+-------------+----------------+----------+")
                if (cheese_inventory < 10 and tomatoes_inventory < 10 and olives_inventory < 10 and mushrooms_inventory < 10):
                    print("|        " + str(cheese_inventory) + "       |      " + str(tomatoes_inventory) + "        |      " + str(olives_inventory) + "      |       " + str(mushrooms_inventory) + "        |    " + str(cash_balance) + "  |")
                
                if (cheese_inventory > 10 and tomatoes_inventory > 10 and olives_inventory > 10 and mushrooms_inventory > 10):
                    print("|       " + str(cheese_inventory) + "       |      " + str(tomatoes_inventory) + "       |      " + str(olives_inventory) + "     |       " + str(mushrooms_inventory) + "       |    " + str(cash_balance) + "  |")
                    
                if (cheese_inventory > 10 and tomatoes_inventory < 10 and olives_inventory < 10 and mushrooms_inventory < 10):
                    print("|       " + str(cheese_inventory) + "       |      " + str(tomatoes_inventory) + "        |      " + str(olives_inventory) + "     |        " + str(mushrooms_inventory) + "        |    " + str(cash_balance) + "  |")
                
                if (cheese_inventory < 10 and tomatoes_inventory > 10 and olives_inventory < 10 and mushrooms_inventory < 10):
                    print("|        " + str(cheese_inventory) + "       |      " + str(tomatoes_inventory) + "       |      " + str(olives_inventory) + "      |       " + str(mushrooms_inventory) + "        |    " + str(cash_balance) + "  |")
                
                if (cheese_inventory < 10 and tomatoes_inventory < 10 and olives_inventory > 10 and mushrooms_inventory < 10):
                    print("|        " + str(cheese_inventory) + "       |      " + str(tomatoes_inventory) + "        |     " + str(olives_inventory) + "      |       " + str(mushrooms_inventory) + "        |    " + str(cash_balance) + "  |")
                    
                if (cheese_inventory < 10 and tomatoes_inventory < 10 and olives_inventory < 10 and mushrooms_inventory > 10):
                    print("|        " + str(cheese_inventory) + "       |      " + str(tomatoes_inventory) + "        |      " + str(olives_inventory) + "      |       " + str(mushrooms_inventory) + "       |    " + str(cash_balance) + "  |")
                
                if (cheese_inventory > 10 and tomatoes_inventory > 10 and olives_inventory < 10 and mushrooms_inventory < 10):
                    print("|       " + str(cheese_inventory) + "       |       " + str(tomatoes_inventory) + "      |      " + str(olives_inventory) + "      |       " + str(mushrooms_inventory) + "        |    " + str(cash_balance) + "  |")
                
                if (cheese_inventory > 10 and tomatoes_inventory < 10 and olives_inventory > 10 and mushrooms_inventory < 10):
                    print("|       " + str(cheese_inventory) + "       |      " + str(tomatoes_inventory) + "        |      " + str(olives_inventory) + "     |        " + str(mushrooms_inventory) + "       |    " + str(cash_balance) + "  |")
                
                if (cheese_inventory > 10 and tomatoes_inventory < 10 and olives_inventory < 10 and mushrooms_inventory > 10):
                    print("|       " + str(cheese_inventory) + "       |      " + str(tomatoes_inventory) + "        |      " + str(olives_inventory) + "      |      " + str(mushrooms_inventory) + "        |    " + str(cash_balance) + "  |")
                
                if (cheese_inventory < 10 and tomatoes_inventory > 10 and olives_inventory > 10 and mushrooms_inventory < 10):
                    print("|        " + str(cheese_inventory) + "       |     " + str(tomatoes_inventory) + "        |      " + str(olives_inventory) + "     |       " + str(mushrooms_inventory) + "        |    " + str(cash_balance) + "  |")
                
                if (cheese_inventory < 10 and tomatoes_inventory > 10 and olives_inventory < 10 and mushrooms_inventory > 10):
                    print("|        " + str(cheese_inventory) + "       |     " + str(tomatoes_inventory) + "        |      " + str(olives_inventory) + "      |       " + str(mushrooms_inventory) + "       |    " + str(cash_balance) + "  |")
                
                if (cheese_inventory < 10 and tomatoes_inventory < 10 and olives_inventory > 10 and mushrooms_inventory > 10):
                    print("|        " + str(cheese_inventory) + "       |      " + str(tomatoes_inventory) + "        |      " + str(olives_inventory) + "     |       " + str(mushrooms_inventory) + "       |    " + str(cash_balance) + "  |")
                    
                    
                print("+----------------+---------------+-------------+----------------+----------+")
                 
                 
                #checking what kind of topping is on the pizza
                
                cheesewanted = 0
                tomatoeswanted = 0
                oliveswanted = 0
                mushroomswanted = 0
                
                if (cheese_inventory > 0):
                    print("You have " + str(cheese_inventory) + " cheese")
                    cheesewanted = input("How much cheese would you like to have in your pizza? \n")
                    cheesewanted = int(cheesewanted)
                    if (cheese_inventory >= cheesewanted):
                        cheese_inventory = cheese_inventory - cheesewanted
                        print("You now have " + str(cheese_inventory) + " cheese left!")                       
                else:
                #checking if all of the cheese is used or not
                    if cheese_inventory == 0:
                        print("You ran out of cheese! \n")
                
                if (tomatoes_inventory > 0):
                    print(" You have " + str(tomatoes_inventory) + " tomatoes")
                    tomatoeswanted = input("How many tomatoes would you like to have in your pizza? \n" )
                    tomatoeswanted = int(tomatoeswanted)
                    if (tomatoes_inventory >= tomatoeswanted):
                        tomatoes_inventory = tomatoes_inventory - tomatoeswanted
                        print("You now have " + str(tomatoes_inventory) + " tomatoes left!")    
                    else:
                        #checking if all of the tomatoes is used or not
                        print("You ran out of tomatoes")
                    
                if (olives_inventory > 0):
                    print("You have " + str(olives_inventory) + " olives")
                    oliveswanted = input("How many olives would you like to have in your pizza? \n")
                    oliveswanted = int(oliveswanted)
                    if (olives_inventory >= oliveswanted):
                        olives_inventory = olives_inventory - oliveswanted         
                        print("You now have " + str(olives_inventory) + " olives left!")                  
                #checking if all of the olives is used or not
                else:
                    print("You ran out of olives")    
                
                if (mushrooms_inventory > 0):
                    print("You have " + str(mushrooms_inventory) + " mushrooms")
                    mushroomswanted = input("How many mushrooms would you like to have in your pizza? \n")
                    mushroomswanted = int(mushroomswanted)
                    if (mushrooms_inventory >= mushroomswanted):
                        mushrooms_inventory = mushrooms_inventory - mushroomswanted    
                        print("You now have " + str(mushrooms_inventory) + " mushrooms left!")                
                #checking if all of the mushrooms are used or not
                else:
                    print("You ran out of mushrooms")
                
                #letting know about the status of the pizza that has been made
                print("You have made a pizza with " + str(cheesewanted) + " cheese, " + str(tomatoeswanted) + " tomatoes, " + str(oliveswanted) + " olives and " + str(mushroomswanted) + " mushrooms")
                
                actual_cost = float((cheesewanted * 1 ) + (tomatoeswanted * 1) + (oliveswanted * 1) + (mushroomswanted * 2))
                print("The actual cost of your pizza is $" + str(actual_cost))
                sellprice = input("How much would you like to sell this pizza for : \nHint: Too high above the the actual cost can result in less sales! \n")
                sellprice = int(sellprice)
                
                if (sellprice >= 2*actual_cost):
                    sales_total = random.randrange ( 200)
                else:
                    sales_total = random.randrange (200, 500)
                    
                revenue = int(sellprice*sales_total)
                profit = int(revenue - actual_cost)
                
                print("Time to get them sales!")
                time.sleep(2)
                print (".");
                time.sleep(2)
                print(".");
                time.sleep(2)
                print(".");
                time.sleep(5);
                print("Opening the Restaurant!")
                time.sleep(10);
                print("Customers are coming in!")
                time.sleep(10);
                print("Closing up for the day!")
                time.sleep(10);
                print("Here are the results of your hard day's work!!!")
                time.sleep(3);
                
                #Displays the remaining ingredients with the selling price of the user's pizza and the profit he gains
                
                print("                            !===========!")
                print("                            !PIZZA SALES!")
                print("                            !===========!")
                print("+----------------+---------------+-------------+----------------+----------+---------+")
                print("|     Cheese     |    Tomatoes   |   Olives    |    Mushrooms   |   Sales  |  Revenue |")
                print("|----------------+---------------+-------------+----------------+----------+---------|")
                print("|        " + str(cheese_inventory) + "       |      " + str(tomatoes_inventory) + "        |      " + str(olives_inventory) + "      |       " + str(mushrooms_inventory) + "        |   " + str(sales_total) + "    |   " + str(revenue) + "  |")
                print("+----------------+---------------+-------------+----------------+----------+---------+")
                
                
                cash_balance += revenue
                print ("Your cash balance is now $" + str(cash_balance))
                #checking the status of profit and sales
                
                if (sellprice == 0):
                    print("You have no sales. You have to work hard!")
                    
                exit = input("Enter any key to go back to main menu : ")
                
        if (main_menu_option == 3):
            
            UTSC = int (250.00)
            conven = int (750.00)
            mall = int (1000)
            
            if (Mall_index != 1):
                print ("Balance: $" + str(cash_balance))
                print ("You can spend your money to upgrade your locations")
                print ("                   +======|============================+")
                print ("                   | S.No |    Location        |  Cost   |")
                print ("                   +======|============================+")
                print ("                   |   1  |       UTSC         | $" +  str(UTSC) + "    |")
                print ("                   +-----------------------------------+")
                print ("                   |   2  |  Conven. Store     | $" + str(conven) + "    |")
                print ("                   +-----------------------------------+")
                print ("                   |   3  |       Mall         | $" + str(mall) + "   |")
                print ("                   +===================================+")
                
                print ("Right now you are located in your " + location + ".")
                print ("Your current cash balance is $" + str(cash_balance))
                
                # if the user can/cannot upgrade at all
                if (cash_balance < UTSC):
                    print ("Sorry, you can't buy any locations")
                    exit = input("Enter any key to go back to the main menu")
                else:    
                    location_choice = input ("Select the number of the location you wish to buy: \nEnter 4 to return to Main Menu \n")
                    location_choice = int(location_choice)                
                    # if the user can/cannot buy location at UTSC
                    
                    if (location_choice == 1):
                    
                        if (UTSC_index == 0):
                            
                            cash_balance = cash_balance - UTSC
                            
                            print ("Congratulations! You are now located at UTSC! Your cash balance is " + "$" + str(cash_balance))
                            exit =  input("Press any key to go back to the main menu")
                            #create variable to add only once - UTSC_index, Conv_index, and Mall_index
                            UTSC_index = 1
                            location = "UTSC"
                            
                        else:
                            
                            print ("You are already located at UTSC!")
                            exit = input("Enter any key to return back to the Main Menu.")
    
                    if (location_choice == 2):
                        if (Conv_index == 0):
                            # if the user can/cannot buy location at convenient store
                            if (cash_balance >= conven):
                                cash_balance = cash_balance - conven
                                print ("Congratulations! You are now located at the Convenience Store! Your cash balance is " + "$" + str(cash_balance))
                                print ("Press any key to go back to the main menu")
                                Conv_index = 1
                                location = "Convenience Store"
                            else:
                                print ("Unable to buy location at conven")
                                exit = input("Press any key to go back to the main menu")
                        else:
                            
                            print ("You are already located at the Convenience Store!")
                            exit = input("Enter any key to return back to the Main Menu.")
                    
                    if (location_choice == 3):     
                        # if the user can/cannot buy location at mall
                        if (Mall_index == 0):
                            if (cash_balance >= mall):
                                cash_balance = cash_balance - mall
                                print ("Congratulations! You are now located at the Mall! You have reached the final level of expansion! Your cash balance is " + "$" + str(cash_balance))
                                exit =  input("Press any key to go back to the main menu")
                                Mall_index = 1
                                location = "Mall"
                                
                            else:
                                print ("You are already located at the Mall!")
                                exit = input("Enter any key to return back to the Main Menu.")   
            else:
                print("You already have the highest level location at the Mall! Congratulations! Now keep selling pizzas and make money to win!")
    
    else:
        print("Thank you very much for playing!")  
        time.sleep(5)
    
    if (Mall_index == 1 and cash_balance >= 10000):
            
        main_menu_option = 4
        print ("CONGRATULATIONS " + player_name + " You are now the most successful Pizza Tycoon! Your Store " + store_name + " will echo through the history of Pizza businesses all over!")        
        time.sleep(5)