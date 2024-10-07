# WITI Academy is proposing a Sacco to help students save their money.
# Design a platform that will do the following . 
# Welcome to , WITIAcademy Sacco.
# 1. Deposit Money 
# 2. Withdraw Money 
# 3. Check Balance 
# Ensure if the student selects 1, money is depsited and minimum deopsit should be 1000.
# If the student selects 2, money should be withdrawn and minimum withdrawal is 500.
# If the student selects 3, the account balance should be displayed.
def sacco_transactions():

    account_balance = 0
    run = 1

    while run == 1:

        print("\nWelcome to, WITIAcademy Sacco.")
# menu
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")

        student_choice = int(input("Enter your selection(1, 2 or 3):"))

        if student_choice == 1:

            print("\n...Processsing a deposit anount transaction... ")
            deposit_amount = int(input("Enter the amount to be deposited: "))

            # check if deposit amount is less than 1000
            if deposit_amount < 1000:
                print('\nMinimum deposit is 1000')
            else:
                account_balance += deposit_amount
                print(f"Dear student you have deposited {deposit_amount:,} and your new account balance is {account_balance:,}")
              

        if student_choice == 2:

            print('\n...Processing a withdraw...')
            withdraw_amount = int(input("Enter the amount to be withdrawn: "))


            if account_balance == 0:
                print("Your account balance is 0")
            elif withdraw_amount < 500:
                print("\nMinimum amount to be withdrawn is 500")
            elif withdraw_amount > account_balance:
                print("Withdraw failed due to insufficient funds")
            else:
                account_balance -= withdraw_amount
                print(f"Dear student, you have withdrawn {withdraw_amount:,} and your new account balance is {account_balance:,}")

            
        elif student_choice == 3:
            print(f"Your account balance is {account_balance:,}")

        else:
            print("You have entered a wrong choice!Select from 1, 2 or 3")

        run = int(input("Enter 1 to continue or any number to exit: "))

        if run != 1:

            print("Thanks for using the SACCO")
            break


sacco_transactions()
