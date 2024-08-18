from functions import *
def main():
    active = True
    acoolstack = DSAstack()
    print(f"Stack created with capacity: {DSAstack.defaultcapacity}.")
    name = input(("What would you like to call your stack? "))
    while active:
            print("\nYou have four options:")
            print("1. Push onto stack.")
            print("2. Pop from stack")
            print("3. Peek at the stack")
            print("4. Check how much in stack")
            print("5. Exit\n")

            choice = int(input("Select an action: "))
            if choice == 1:
                try:
                    print(f"You have chosen to push onto your stack, {name}")
                    pushingthing = input(f"What would you like to push onto your stack, {name}? ")
                    acoolstack.push(pushingthing)
                    anotherchoice = input("Would you like to push more?(Y/N) ")
                    while anotherchoice == "Y" or anotherchoice == "Yes":
                        pushingthing = input(f"What would you like to push onto your stack, {name}? ")
                        acoolstack.push(pushingthing)
                        anotherchoice = input("Would you like to push more?(Y/N) ")
                        if anotherchoice == "N" or anotherchoice == "No":
                            print("Returning to main menu:")
                except Exception as e:
                    print("An error occurred:", e)

            elif choice == 2:
                try:
                    print(f"You have chosen to pop from your stack, {name}")
                    poppedvalue = acoolstack.pop()
                    print(f"The value you have popped is: {poppedvalue}")  
                    anotherchoice = input("Would you like to pop more?(Y/N) ")
                    while anotherchoice == "Y" or anotherchoice == "Yes":
                        poppedvalue = acoolstack.pop()
                        print(f"The value you have popped is: {poppedvalue}") 
                        anotherchoice = input("Would you like to pop more?(Y/N) ") 
                        if anotherchoice == "N" or anotherchoice == "No":
                            print("Returning to main menu:")
                except Exception as e:
                    print("An error occurred:", e)

            elif choice == 3:
                try:
                    print(f"You have chosen to peek at your stack, {name}.")
                    topvalue = acoolstack.top()
                    print(f"The top value for {name} is: {topvalue}")
                except Exception as e:
                    print("An error occurred:", e)                

            elif choice == 4:
                try:
                    print(f"You have chosen to see how many elements are in your stack, {name}")
                    print(f"You have {acoolstack.getCount()} elements in {name}")
                except Exception as e:
                        print("An error occurred:", e)                
                
            elif choice == 5:
                print("Thank you for using the program!")
                active = False


if __name__ == "__main__":
    main()