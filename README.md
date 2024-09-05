# Fitracker

Fitracker is a command-line calorie tracking application that allows users to log their meals, workouts, and monitor their daily calorie intake and expenditure.

## Author

Rodolfo Lopez

## Date

Fall 2021

## Features

- User registration and login system
- Secure password storage using Caesar Cipher encryption
- Create and edit user profiles with personal details
- Log custom meals and drinks
- Log custom workouts (cardio and weighted exercises)
- Calculate daily calorie budget based on user information
- Track daily calorie consumption and expenditure
- Display daily calorie totals and progress
- Save daily progress to a user-specific file

## Files

- `app.py`: Main application file containing the core functionality
- `account.py`: Defines the Account class for user profiles
- `day.py`: Defines the Day class for tracking daily progress
- `meal.py`: Defines the Meal, Food, and Drink classes
- `workout.py`: Defines the Workout, Cardio, and Weighted classes
- `accounts.json`: Stores user account information
- `credentials.json`: Stores encrypted user login credentials
- `meals.json`: Stores custom meal and drink information
- `workouts.json`: Stores custom workout information

## Usage

1. Run `app.py` to start the application
2. Choose to login, register, or quit
3. If registering, create an account and enter personal details
4. Once logged in, use the tracker menu to:
   - View daily calorie totals
   - Add meals and drinks
   - Add workouts
   - Edit account information
   - Check progress
   - Finish logging for the day

## Requirements

- Python 3.x

## Installation

1. Clone the repository
2. Ensure you have Python 3.x installed
3. Run `python app.py` to start the application

## Future Improvements

- Implement a graphical user interface
- Add data visualization for progress tracking
- Integrate with fitness tracking devices or apps
- Implement a database for more efficient data storage
