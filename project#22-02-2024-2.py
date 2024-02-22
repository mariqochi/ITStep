import csv
from datetime import datetime, timedelta


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
       
        register_choice = input("Do you have an account? (y/n): ")
        if register_choice.lower() == 'n':
            while True:
                username = input("Enter username for registration: ")
                password = input("Enter your password: ")
                try:
                    self.add_user(username, password)
                    print("User registration successful.")
                    break
                except ValueError:
                    print("Username already exists. Please choose a different username.")
        elif register_choice.lower() == 'y':
            self.username = input("Enter your username: ")
            self.password = input("Enter your password: ")
            print("Login successful.")
        else:
            print("Invalid choice.")

    def add_user(self, username, password):
        # Add logic to add user to database
        pass


class VATRegistration(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.turnover_records = {}
        self.vat_registered = False

    def add_turnover(self, date, turnover):
        self.turnover_records[date] = turnover

    def update_turnover(self, date, new_turnover):
        if date in self.turnover_records:
            self.turnover_records[date] = new_turnover
            print(f"Turnover for {date} updated successfully.")
        else:
            print(f"No turnover recorded for {date}.")

    def display_turnover(self):
        total_turnover = sum(self.turnover_records.values())
        print(f"Total turnover: {total_turnover}")
        for date, turnover in self.turnover_records.items():
            print(f"Turnover for {date}: {turnover}")

    def calculate_vat_threshold(self, date):
        total_turnover = sum(self.turnover_records.values())
        return total_turnover >= 100000

    def get_registration_deadline(self):
        today = datetime.now().date()
        days_until_deadline = 2  
        while days_until_deadline > 0:
            today += timedelta(days=1)
            if today.weekday() < 5:  
                days_until_deadline -= 1
        return today

    def register_turnover(self):
        while True:
            date_str = input("Enter turnover date (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                if date > datetime.now().date():
                    print("Cannot enter turnover for future date.")
                    continue
                turnover = float(input("Enter daily turnover: "))
                if turnover < 0:
                    print("Turnover cannot be negative.")
                    continue
                self.add_turnover(date, turnover)
                print("Turnover registered successfully.")

                # Check if VAT registration is required
                if not self.vat_registered and self.calculate_vat_threshold(date):
                    deadline = self.get_registration_deadline()
                    print(f"You must register for VAT. The deadline is {deadline.strftime('%Y-%m-%d')}.")
                    self.vat_registered = True
            except ValueError:
                print("Invalid date format or turnover amount.")

            choice = input("Do you want to register another turnover? (y/n): ")
            if choice.lower() != 'y':
                break
            
            self.save_to_csv("turnover_records.csv")

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Date', 'Turnover']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for date, turnover in self.turnover_records.items():
                writer.writerow({'Date': date.strftime("%Y-%m-%d"), 'Turnover': turnover})



user_reg = User(None, None)
user_reg.register()

vat_reg = VATRegistration(user_reg.username, user_reg.password)
vat_reg.register_turnover()
vat_reg.display_turnover()

