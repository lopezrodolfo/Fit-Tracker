import json

from account import Account
from day import Day
from meal import *
from workout import *


def cipher(password, shift):
    """Cesar Cipher to encrypt/decrypt passwords from credentials.json"""
    text = ""
    for sym in password:
        if sym == " ":
            text += sym
        elif sym.isupper():
            text += chr((ord(sym) + shift - 65) % 26 + 65)
        else:
            text += chr((ord(sym) + shift - 97) % 26 + 97)
    return text


def login(shift):
    """Returns logged in user or quits. Reads credentials.json"""
    with open("credentials.json") as f:
        users = json.load(f)

    # username check
    username = ""
    username_valid = False
    while not username_valid:
        username = input("Enter username or (Q)Quit:\n")
        if username == "q" or username == "Q":
            destroy()

        for user in users:
            if user["username"] == username:
                username_valid = True
                break
        if not username_valid:
            print("Username does not exist. Try again.")

    # password check
    password = ""
    password_valid = False

    while not password_valid:
        password = input("Enter password or Q(Quit)\n")
        if password == "q" or password == "Q":
            destroy()
        for user in users:
            if user["username"] == username and user["password"] == cipher(
                password, shift
            ):
                password_valid = True
        if not password_valid:
            print("Invalid Password. Try Again.")

    return username


def register(shift):
    """Returns registered user or quits. Writes credentials.json"""
    with open("credentials.json") as f:
        users = json.load(f)

    # username check
    username = ""
    while True:
        username = input("Enter username or (Q)Quit:\n")
        if username == "q" or username == "Q":
            destroy()
        username_invalid = False
        if users:
            for user in users:
                if user["username"] == username:
                    username_invalid = True
                    print("Username already exists. Try again")
                    break
            if username_invalid:
                continue
            else:
                break
        else:
            username_invalid = True

    # password check
    password = ""
    while True:
        password = input("Enter password or Q(Quit)\n")
        if password == "q" or password == "Q":
            destroy()

        confirm_password = input("Confirm password\n")
        if password != confirm_password:
            print("Password mismatch. Try again.")
            continue
        else:
            break

    users.append({"username": username, "password": cipher(password, shift)})

    with open("credentials.json", "w") as f:
        json.dump(users, f, indent=4, separators=(",", ": "))

    return username


def editAccount(userAcc):
    """returns Account object of registered user. Edits accouts.json"""
    # account details effecting calorie budget
    while True:
        height = input("Enter height in inches:\n")
        if not height.isdecimal():
            print("Needs to be a number")
            continue
        break
    while True:
        weight = input("Enter weight in pounds:\n")
        if not weight.isdecimal():
            print("Needs to be a number")
            continue
        break
    while True:
        age = input("Enter age:\n")
        if not age.isnumeric():
            print("Needs to be a number")
            continue
        break

    # init will perform calorie computations with respect to some of the account params
    curAccount = Account(
        userAcc.username, userAcc.full_name, userAcc.gender, height, weight, age
    )

    with open("accounts.json") as f:
        accounts = json.load(f)

    for account in accounts:
        if account["username"] == curAccount.username:
            accounts.remove(account)
            accounts.append(
                {
                    "username": str(curAccount.username),
                    "full name": str(curAccount.full_name),
                    "gender": str(curAccount.gender),
                    "height": str(curAccount.height),
                    "weight": str(curAccount.weight),
                    "age": str(curAccount.age),
                    "calories consumed": str(curAccount.calories_consumed),
                    "calories burned": str(curAccount.calories_burned),
                    "calorie budget": str(curAccount.calorie_budget),
                    "net calories": str(curAccount.net_calories),
                    "deviation": str(curAccount.deviation),
                }
            )
            break

    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4, separators=(",", ": "))

    return curAccount


def makeAccount(cur_username):
    """returns Account object of registered user. Writes accouts.json"""

    # account details
    full_name = input("Enter full name:\n")
    gender = input("Enter gender:\n")
    while True:
        height = input("Enter height in inches:\n")
        if not height.isdecimal():
            print("Needs to be a number")
            continue
        break
    while True:
        weight = input("Enter weight in pounds:\n")
        if not weight.isdecimal():
            print("Needs to be a number")
            continue
        break
    while True:
        age = input("Enter age:\n")
        if not age.isnumeric():
            print("Needs to be a number")
            continue
        break

    # init will perform calorie computations with respect to some of the account params (bmr)
    curAccount = Account(cur_username, full_name, gender, height, weight, age)

    with open("accounts.json") as f:
        accounts = json.load(f)

    accounts.append(
        {
            "username": curAccount.username,
            "full name": curAccount.full_name,
            "gender": curAccount.gender,
            "height": str(curAccount.height),
            "weight": str(curAccount.weight),
            "age": str(curAccount.age),
            "calories consumed": str(curAccount.calories_consumed),
            "calories burned": str(curAccount.calories_burned),
            "calorie budget": str(curAccount.calorie_budget),
            "net calories": str(curAccount.net_calories),
            "deviation": str(curAccount.deviation),
        }
    )

    # save account details
    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4, separators=(",", ": "))

    return curAccount


def getAccount(cur_username):
    """returns Account object of registered user"""

    # account already made
    with open("accounts.json") as f:
        accounts = json.load(f)

    for account in accounts:
        if account["username"] == cur_username:
            return Account(
                account["username"],
                account["full name"],
                account["gender"],
                account["height"],
                account["weight"],
                account["age"],
            )

    # handles account creation if a user registered but exited the program before account was made
    print("You need to create an account in order to use the tracker")

    while True:
        option = input("(A)Account (Q)Quit\n").lower()
        if option != "a" and option != "q":
            print("Invalid option. Try again.")
            continue
        elif option == "q":
            destroy()
        else:
            print("Make Account")
            return makeAccount(cur_username)


def saveWeighted(weighted):
    """Writes weighted to workouts.json database"""
    # save new Weighted workout for user or other users
    with open("workouts.json") as f:
        workouts = json.load(f)

    workouts.append(
        {
            "type": "weighted",
            "name": weighted.name,
            "caloriesPerHour": str(weighted.calories_per_hour),
            "hours": str(weighted.hours),
        }
    )

    with open("workouts.json", "w") as f:
        json.dump(workouts, f, indent=4, separators=(",", ": "))


def saveCardio(cardio):
    """Writes cardio to workouts.json database"""
    # save new Cardio workout for user or other users
    with open("workouts.json") as f:
        workouts = json.load(f)

    workouts.append(
        {
            "type": "cardio",
            "name": cardio.name,
            "caloriesPerHour": str(cardio.calories_per_hour),
            "hours": str(cardio.hours),
        }
    )

    with open("workouts.json", "w") as f:
        json.dump(workouts, f, indent=4, separators=(",", ": "))


def getCardio():
    """returns user created cardio object"""

    cardio_name = input("Enter cardio workout name:\n").lower()

    while True:
        cardio_calories_per_hour = input(
            "Enter the amount of calories burned in one hour of perfroming the cardio workout:\n"
        )
        if not cardio_calories_per_hour.isdecimal():
            print("Needs to be number")
            continue
        break

    while True:
        cardio_hours = input("Enter time in hours spent on the cardio workout:\n")
        if not cardio_hours.isdecimal():
            print("Needs to be number")
            continue
        break

    # create Cardio workout
    cardio_workout = Cardio(cardio_name, cardio_calories_per_hour, cardio_hours)

    return cardio_workout


def getWeighted():
    """returns user created weighted object"""

    weighted_name = input("Enter weighted workout name:\n").lower()

    while True:
        weighted_calories_per_hour = input(
            "Enter the amount of calories burned in one hour of performing the weighted exercise:\n"
        )
        if not weighted_calories_per_hour.isdecimal():
            print("Needs to be number")
            continue
        break

    while True:
        weighted_hours = input("Enter time in hours spent on the weighted workout:\n")
        if not weighted_hours.isdecimal():
            print("Needs to be number")
            continue
        break

    # create Weighted workout
    weighted_workout = Weighted(
        weighted_name, weighted_calories_per_hour, weighted_hours
    )

    return weighted_workout


def addCustomWorkout(curAccount):
    """returns account with added custom workout accounted for"""

    sub_choice = input("(1)Add Cardio Workout (2)Add Weighted Workout\n")
    # cardio
    if sub_choice == "1":
        # create Cardio workout
        cardio_workout = getCardio()

        # account calories burned inc
        curAccount.incCaloriesBurned(cardio_workout.calcCaloriesBurned())

        # writes cardio to json file
        saveCardio(cardio_workout)
        print("Cardio Workout saved to database. Make sure to save in account after.")

        return curAccount

    # weighted
    elif sub_choice == "2":
        # create Weighted workout
        weighted_workout = getWeighted()

        # account calories burned decremented
        curAccount.incCaloriesBurned(weighted_workout.calcCaloriesBurned())

        # writes weighted to json file
        saveWeighted(weighted_workout)
        print("Weighted Workout saved to database but account still needs saving")

        return curAccount


def addExistingWorkout(curAccount):
    """returns account with added existing workout accounted for"""

    with open("workouts.json") as f:
        workouts = json.load(f)

    sub_choice = input("(1)Add Cardio (2)Add Weighted\n")
    # cardio
    if sub_choice == "1":
        cardio_workout = getCardio()

        dne = True
        for workout in workouts:
            if workout["type"] == "cardio":
                if (
                    workout["name"] == cardio_workout.name
                    and workout["caloriesPerHour"] == cardio_workout.calories_per_hour
                    and workout["hours"] == cardio_workout.hours
                ):
                    dne = False

                    # increment account's calories consumed that will be returned
                    curAccount.incCaloriesBurned(cardio_workout.calcCaloriesBurned())
                    print("Existing cardio workout was logged but not saved")
                    return curAccount
        if dne:
            print("Cardio workout does not exist in database")
            return curAccount

    # weighted
    elif sub_choice == "2":
        weighted_workout = getWeighted()

        dne = True
        for workout in workouts:
            if workout["type"] == "weighted":
                if (
                    workout["name"] == weighted_workout.name
                    and workout["caloriesPerHour"] == weighted_workout.calories_per_hour
                    and workout["hours"] == weighted_workout.hours
                ):
                    dne = False

                    # increment account's calories consumed that will be returned
                    curAccount.incCaloriesBurned(weighted_workout.calcCaloriesBurned())

                    print("Existing weighted workout was logged but not saved")
                    return curAccount
        if dne:
            print("Weighted workout does not exist in database")
            return curAccount


def addWorkout(curAccount):
    """Returns modified account in regard to logged workouts"""

    while True:
        # user choices for workout add
        choice = input(
            "(1)Add custom workout (2)Add existing workout (3)Stop adding workouts\n"
        )
        # custom workout
        if choice == "1":
            curAccount = addCustomWorkout(curAccount)

        # existing workout
        elif choice == "2":
            curAccount = addExistingWorkout(curAccount)

        # return modified account to tracker
        elif choice == "3":
            return curAccount


def saveDrink(drink):
    """Writes drink to meals.json database"""
    # save new Food for user or other users
    with open("meals.json") as f:
        meals = json.load(f)

    meals.append(
        {
            "type": "drink",
            "name": drink.name,
            "unit": drink.unit,
            "caloriesPerUnit": str(drink.calories_per_unit),
            "amount": str(drink.amount),
        }
    )

    with open("meals.json", "w") as f:
        json.dump(meals, f, indent=4, separators=(",", ": "))


def saveFood(food):
    """Writes food to meals.json database"""
    # save new Food for user or other users
    with open("meals.json") as f:
        meals = json.load(f)

    meals.append(
        {
            "type": "food",
            "name": food.name,
            "unit": food.unit,
            "caloriesPerUnit": str(food.calories_per_unit),
            "amount": str(food.amount),
        }
    )

    with open("meals.json", "w") as f:
        json.dump(meals, f, indent=4, separators=(",", ": "))


def getFood():
    """returns user created food object"""

    food_name = input("Enter the food's name:\n").lower()

    while True:
        food_measure_unit = input(
            "Food is measured in (C)Cups (G)Grams (O)Other?\n"
        ).lower()
        if food_measure_unit == "c":
            unit = "cup"
            break
        elif food_measure_unit == "g":
            unit = "gram"
            break
        elif food_measure_unit == "o":
            unit = input(
                "Enter custom measure unit (eg serving size, bag, can, etc.):\n"
            ).lower()
            break
        else:
            print("Invalid Option")
            continue

    while True:
        food_calories_per_unit = input(f"Enter the food's calories per {unit}:\n")
        if not food_calories_per_unit.isdecimal():
            print("Needs to be number")
            continue
        break

    while True:
        food_amount = input(f"Enter the amount of this food consumed in {unit}s:\n")
        if not food_amount.isdecimal():
            print("Needs to be number")
            continue
        break

    # create Food
    food_meal = Food(food_name, unit, food_calories_per_unit, food_amount)

    return food_meal


def getDrink():
    """returns user created drink object"""

    drink_name = input("Enter drink's name:\n").lower()

    while True:
        drink_measure_unit = input("Measure in (C)Cups (G)Grams (O)Other?\n").lower()
        if drink_measure_unit == "c":
            unit = "cup"
            break
        elif drink_measure_unit == "g":
            unit = "gram"
            break
        elif drink_measure_unit == "o":
            unit = input(
                "Enter custom measure unit (eg serving size, bag, can, etc.):\n"
            ).lower()
            break
        else:
            print("Invalid Option")
            continue

    while True:
        drink_calories_per_unit = input(f"Enter drink's calories per {unit}:\n").lower()
        if not drink_calories_per_unit.isdecimal():
            print("Needs to be number")
            continue
        break

    while True:
        drink_amount = input(f"Enter the amount of this drink consumed in {unit}s:\n")
        if not drink_amount.isdecimal():
            print("Needs to be number")
            continue
        break

    # create Drink
    drink_meal = Drink(drink_name, unit, drink_calories_per_unit, drink_amount)

    return drink_meal


def addCustomMeal(curAccount):
    """returns account with added custom meal accounted for"""
    sub_choice = input("(1)Add Food (2)Add Drink\n")
    # food
    if sub_choice == "1":
        # create Food
        food_meal = getFood()

        # increment account's calories consumed that will be returned
        curAccount.incCaloriesConsumed(food_meal.calcCaloriesConsumed())

        # writes food to json file
        saveFood(food_meal)
        print("Food added to database but not saved under account yet")

        return curAccount

    # drink
    elif sub_choice == "2":
        # create Drink
        drink_meal = getDrink()

        # increment account's calories consumed that will be returned
        curAccount.incCaloriesConsumed(drink_meal.calcCaloriesConsumed())

        # saves drink to json file
        saveDrink(drink_meal)
        print("Drink added to database but not saved under account yet")

        return curAccount


def addExistingMeal(curAccount):
    """returns account with added existing meal accounted for"""
    with open("meals.json") as f:
        meals = json.load(f)

    sub_choice = input("(1)Add Food (2)Add Drink\n")
    # food
    if sub_choice == "1":
        food_meal = getFood()

        dne = True
        for meal in meals:
            if meal["type"] == "food":
                if (
                    meal["name"] == food_meal.name
                    and meal["unit"] == food_meal.unit
                    and meal["caloriesPerUnit"] == food_meal.calories_per_unit
                    and meal["amount"] == food_meal.amount
                ):
                    dne = False

                    # increment account's calories consumed that will be returned
                    curAccount.incCaloriesConsumed(food_meal.calcCaloriesConsumed())
                    print(
                        "Existing food meal was logged but not saved under account yet"
                    )
                    return curAccount
        if dne:
            print("Food does not exist in database")
            return curAccount

    # drink
    elif sub_choice == "2":
        drink_meal = getDrink()

        dne = True
        for meal in meals:
            if meal["type"] == "drink":
                if (
                    meal["name"] == drink_meal.name
                    and meal["unit"] == drink_meal.unit
                    and meal["caloriesPerUnit"] == drink_meal.calories_per_unit
                    and meal["amount"] == drink_meal.amount
                ):
                    dne = False

                    # increment account's calories consumed that will be returned
                    curAccount.incCaloriesConsumed(drink_meal.calcCaloriesConsumed())
                    print(
                        "Existing drink meal was logged but not saved under account yet"
                    )
                    return curAccount
        if dne:
            print("Drink does not exist in database")
            return curAccount


def addMeal(curAccount):
    """Returns modified account in regard to logged meals"""

    while True:
        # user choices for meal add
        choice = input("(1)Add custom meal (2)Add existing meal (3)Stop adding meals\n")
        # custom meal
        if choice == "1":
            curAccount = addCustomMeal(curAccount)

        # existing meal
        elif choice == "2":
            curAccount = addExistingMeal(curAccount)

        # return modified account to tracker
        elif choice == "3":
            return curAccount


def saveTrackedAccount(curAccount):
    """saves all meals and workouts tracked into accounts.json"""
    with open("accounts.json") as f:
        accounts = json.load(f)

    for account in accounts:
        if account["username"] == curAccount.username:
            accounts.remove(account)
            accounts.append(
                {
                    "username": str(curAccount.username),
                    "full name": str(curAccount.full_name),
                    "gender": str(curAccount.gender),
                    "height": str(curAccount.height),
                    "weight": str(curAccount.weight),
                    "age": str(curAccount.age),
                    "calories consumed": str(curAccount.calories_consumed),
                    "calories burned": str(curAccount.calories_burned),
                    "calorie budget": str(curAccount.calorie_budget),
                    "net calories": str(curAccount.net_calories),
                    "deviation": str(curAccount.deviation),
                }
            )
            break

    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4, separators=(",", ": "))


def displayProgress(curAccount):
    curDay = Day(curAccount)
    curAccountProgFileName = curAccount.username + "prog.txt"
    try:
        with open(curAccountProgFileName) as f:
            print("Progress")
            for prog in f:
                print(prog)
    except IOError:
        print(
            "You have not tracked any days yet. So there is no calorie progress to display"
        )


def tracker(curAccount):
    """Log meals/workouts. Display Daily Totals/Progress. Edit Account."""

    # user tracker options
    while True:
        option = input(
            "(D)Daily-Calorie-Totals (M)Meal-Add (W)Workout-Add (E)Edit-Account (P)Progress Check (F)Finished Logging\n"
        ).lower()
        # daily calorie totals
        if option == "d":
            print(curAccount)
        # log meal
        elif option == "m":
            print("Add Meal")
            curAccount = addMeal(curAccount)  # calorie_consumed updated for account
            print("Meal Added")
        # log workout
        elif option == "w":
            print("Add Workout")
            curAccount = addWorkout(curAccount)  # calorie_burned updated for account
            print("Workout Added")
        # edit account
        elif option == "e":
            print("Edit Account")
            curAccount = editAccount(curAccount)
            print("Editted Account")
        # progress check
        elif option == "p":
            displayProgress(curAccount)
        # save tracked account
        elif option == "f":
            saveTrackedAccount(curAccount)
            print("Saved Account")
            break
        # invalid option
        else:
            print("Please enter a valid option")

    return curAccount


def destroy():
    """Ends program"""
    print("Thanks for tracking!")
    exit()


def saveProgOrQuit(curAccount):
    """saves daily calories totals for each user or ends program"""
    while True:
        option = input(
            "Would you like to save daily calorie totals to your progress file? Yes or No:\n"
        ).lower()
        if option == "n" or option == "no":
            destroy()
        elif option == "y" or option == "yes":
            curAccountProgFileName = curAccount.username + "prog.txt"
            curDay = Day(curAccount)
            with open(curAccountProgFileName, "a") as f:
                f.write(f"Date: {curDay.date} {curAccount}")
            print("Your tracked calorie progress has been saved for today")
            destroy()
        else:
            print("Invalid Option")
            continue


def app():
    """Handles state of fitness tracker"""
    print("Welcome to Fitracker!")
    cur_username = ""
    shift = 4  # shift used to cipher passwords
    # user start options
    option = input("Menu: (L)Login (R)Register (Q)Quit:\n").lower()
    while True:
        # login
        if option == "l":
            print("Login")
            cur_username = login(shift)
            print("Logged In")
            curAccount = getAccount(cur_username)
            print("Tracker")
            curAccount = tracker(curAccount)
            print("Finished Tracking")
            saveProgOrQuit(curAccount)
        # register
        elif option == "r":
            print("Register")
            cur_username = register(shift)
            print("Registered")
            print("Make Account")
            curAccount = makeAccount(cur_username)
            print("Made Account")
            option = "l"
            continue
        # quit
        elif option == "q":
            destroy()
        # invalid option
        else:
            print("Please enter a valid option")
            option = input("Menu: (L)Login (R)Register (Q)Quit:\n").lower()
            continue


if __name__ == "__main__":
    app()
