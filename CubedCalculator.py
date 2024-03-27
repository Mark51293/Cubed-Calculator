
lines = ("-" * 50)
welcome = "        Welcome to the cubed calculator!"


print(f"{lines}\n{welcome}\n{lines}\n\n")


user_number = int(input("Enter a number greater than 0: "))

while user_number <= 0:
    user_number = int(input("Please try again: "))

if user_number >= 0:
    print(user_number ** 3)
    user_selection = str(input("Do you want to go again? y/n: "))

    if user_selection == "y":
        
        while user_selection == "y":
            
            user_number = int(input("Enter a number greater than 0: "))
            
            if user_number <=0:
            
                print("Try again: ")
                user_number = int(input("Enter a number greater than 0: "))
            
            else:
                print(user_number ** 3)
                user_selection = str(input("Do you want to go again? y/n: "))

            if user_selection == "n":
                print("Goodbye! (:")
    else:
        print("Goodbye! (:")

    
    
   





