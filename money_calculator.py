from datetime import datetime
# #input amount you want to save
# amount_to_save = input("How much do you want to save ?: $" )

# While loop to validate format
while True:
    try:
        # Get today's date for comparison
        today = datetime.today()

        #Take separate inputs
        day = int(input("Enter the day you want to save by (1-31): "))
        # Validation
        if day < 1 or day > 31:
            print("Day must be between 1 and 31.")
            continue
        month = int(input("Enter the month (1-12): "))
        # Validation
        if month < 1 or month > 12:
            print("Month must between 1 and 12.")
            continue
        year = int(input("Enter the year:"))
        # Validation
        if 25 <= year <= 99:
            year = 2000 + year
        elif 2025 <= year <=2099:
            year = year
        else:
            print("Year must be 2025 or later.")
            continue

        #Try to create a date object
        save_date = datetime(year,month,day)

        #Check if date is in future
        if save_date <= today:
            print("Date must be in the future.")
            continue

        #If date is valid
        print("You Entered:", save_date.strftime("%d-%m-%Y"))

        #weeks remaining to save
        time_remaining = round((save_date - today).days / 7)
        print(f"Weeks remaining until save by date:{round(time_remaining)} weeks")

        while True:
            # input of amount to be saved
            goal_amount = float(input("What amount do you want to save?: $"))
            if goal_amount <= 0:
                print("Goal amount must be more than $0")
                continue
            break
        weekly_saving = round(goal_amount / time_remaining)

        print(f"If you want to save ${goal_amount} by {save_date.strftime("%d-%m-%Y")}, then you must save ${weekly_saving} across {time_remaining} weeks.")
        break

    except ValueError:
        print("Invalid date format! Please use DD-MM-YY.")
