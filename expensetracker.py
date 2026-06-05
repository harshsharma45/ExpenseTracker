#Expense Tracker

def main():
    print("Expense Tracker Using Python")
    my_expense = []
    total = 0
    print("Welcome to the Expense Tracker")
    print("Enter your choice:")
    while True:
        print("1.Add Expenses")
        print("2.Remove Expenses")
        print("3.Total Expenses")
        print("4.Quit")

        try:
            choice = int(input("Enter your choice:"))
            if choice == 1:
                n = int(input("Enter the number to data to enter:"))
                if n==0:
                    print("Please try again")
                else:
                    for i in range(n):
                        ex_inp=float(input("Enter the data:"))
                        my_expense.append(ex_inp)
                        total = sum(my_expense)
                print("Total Expense =",total)
                print("Your Expenses = ",my_expense)

            elif choice == 2:
                if total ==0:
                    print("No expenses to remove")
                else:
                    remove_exp = float(input("Enter the data to delete:"))
                    if remove_exp not in my_expense:
                        print("Data not found to delete")
                    else:
                        my_expense.remove(remove_exp)
                        total = sum(my_expense)
                        print("Your Expenses=",my_expense)
                        print("Remaining Expenses = ",sum(my_expense))



            elif choice == 3:
                if total == 0:
                    print("You have no expenses")
                else:
                    print("Total Expenses=",total)
                    print("Number of Expenses = ",len(my_expense))


            elif choice == 4:
                print("Quit")
                print("Thank You for using Our Program")
                break

            else:
                print("Invalid Input! , Please Try Again")

        except ValueError:
            print("Please Enter a Valid Choice")

if __name__ == "__main__":
    main()