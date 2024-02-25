#დღგ-ს რეგისტრაციის ზღვარის გამოთვლა

import csv
from datetime import datetime, timedelta
import os

class User:    # მომხმარებლის კლასის შექმნა ატრიბუტებით პაროლი და სახელი
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):   #მეთოდი: იმ შემთხვევაში თუ მომხმარებელი რეგისტრირებულია ციკლი წყდება 
        while True:
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
                break  # სრულდება თუ მომხამრებელი წარმატებით რეგისტრირდება
            elif register_choice.lower() == 'y':
                while True:
                    self.username = input("Enter your username: ")
                    self.password = input("Enter your password: ")
                    if self.login(self.username, self.password):
                        print("Login successful.")
                        self.load_turnover_records()  # #მოწმდება თუ არის რეგისტრირებულ მომხამრებლებში მომხმარებლის სახელი
                        self.process_turnover_registration()  # vat class 
                        break  
                    else:
                        retry_choice = input("Invalid username or password. Retry? (y/n): ")
                        if retry_choice.lower() != 'y':
                            break  
                break  
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
                continue  

    def login(self, username, password):   ##ატვირთულ მონაცემებში შესაბამისი მომხმარებლის გადამოწმება და შემდეგ მისი პასწორდის გადამოწმება სისტემაში შესვლისას
        with open('registered_users.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2 and row[0] == username and row[1] == password:
                    return True
        return False

    def add_user(self, username, password):   # მომხმარებლის რეგისტრაციისას ატვირთულ მონაცემებში არსებული მომხმარებლის სახელის გადამოწმება, რომ არ განმეორდეს მომხმარებლის სახელი
        if os.path.exists('registered_users.csv'):
            with open('registered_users.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                existing_usernames = [row[0] for row in reader if row]
                if username in existing_usernames:
                    raise ValueError("Username already exists.")

        with open('registered_users.csv', 'a') as csvfile:  # თუ მომხმარებლის სახელი არ იძებნება არსებულ მონაცემებში, ხდება მისი დამატება
            writer = csv.writer(csvfile)
            writer.writerow([username, password])  

    def process_turnover_registration(self):  # აკავშირებს შეყვანილ მონაცემებს უსერის სახელით და შეაქვს CSV ფაი₾ში
        choice = input("Do you want to register turnover? (y/n): ")
        if choice.lower() == 'y':
            vat_reg = VATRegistration(self.username, self.password)
            vat_reg.load_turnover_records()  # შესაბამისი მომხამრებლის ბრუნვებს ჩამოტვირთავს
            vat_reg.register_turnover()
        else:
            # If user chooses not to register turnover, display total turnover
            self.load_turnover_records()  # Load turnover records for the logged-in user
            self.display_turnover()

    def load_turnover_records(self):   # ბრუნვის შესახებ მონაცემების შენახვის მეთოდი CVS ფაილში
        filename = f"{self.username}_turnover_records.csv"
        if os.path.exists(filename):
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                self.turnover_records = {datetime.strptime(row['Date'], "%Y-%m-%d").date(): float(row['Turnover']) for row in reader}
        else:
            self.turnover_records = {}

    def display_turnover(self):    #მიმდინარე 12 თვის ბრუნვის გამოტანის მეთოდი
        last_year_date = datetime.now() - timedelta(days=365)
        last_year_date = datetime(last_year_date.year, 3, 1)  # Start counting from March of last year
        total_turnover = sum(amount for date, amount in self.turnover_records.items() if date >= last_year_date.date())
        print(f"Total turnover for the last 12 months: {total_turnover}")
        for date, turnover in sorted(self.turnover_records.items()):
            if date >= last_year_date.date():
                print(f"Turnover for {date}: {turnover}")


class VATRegistration:    #VAT  კლასი
    def __init__(self, username, password): # გაეშვება მომხმარებლის სახელით და პააროლით რეგისტრირებული ბრუნვები
        self.username = username
        self.password = password
        self.turnover_records = {}
        self.vat_registered = False
        self.threshold_reached_date = None  #ინახავს ბრუნვის ზღვარზე გადაჭარბების თარიღს

    def get_registration_deadline(self, threshold_reached_date):   # დედალიანის თრაიღის გამოთვლა
        days_until_deadline = 2
        deadline = threshold_reached_date + timedelta(days=days_until_deadline)
       
        while days_until_deadline > 0:
            deadline += timedelta(days=1)
            if deadline.weekday() < 5:
                days_until_deadline -= 1
        return deadline

    def add_turnover(self, date, turnover):    
        self.turnover_records[date] = turnover

    def display_turnover(self):
        last_year_date = datetime.now() - timedelta(days=365)
        last_year_date = datetime(last_year_date.year, 3, 1)  
        total_turnover = sum(amount for date, amount in self.turnover_records.items() if date >= last_year_date.date())
        print(f"Total turnover for the last 12 months: {total_turnover}")
        for date, turnover in sorted(self.turnover_records.items()):
            if date >= last_year_date.date():
                print(f"Turnover for {date}: {turnover}")

    def calculate_vat_threshold(self, date):   #თანხის გამოთვლა დედლაინისთვის
        last_year_date = datetime.now() - timedelta(days=365)
        last_year_date = datetime(last_year_date.year, 3, 1) 
        total_turnover = sum(amount for date, amount in self.turnover_records.items() if date >= last_year_date.date())
        return total_turnover >= 100000

    def register_turnover(self):   #დღიური ბრუნვის რეგისტრაციის მეთოდი
        self.load_turnover_records()  # 
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

                
                if date in self.turnover_records: #ამოწმებს თუ არის აღნიშნული თარიღი რეგისტრირებული
                    
                    self.turnover_records[date] += turnover
                else:
                   
                    self.turnover_records[date] = turnover  #თუ არ არუს ქმნის ახალ ჩანაწერს

                print("Turnover registered successfully.")

                if not self.vat_registered and self.calculate_vat_threshold(date):
                    self.threshold_reached_date = date  
                    deadline = self.get_registration_deadline(self.threshold_reached_date)
                    if deadline:
                        print(f"You must register for VAT. The deadline is {deadline.strftime('%Y-%m-%d')}.")  #თუ გადააჭარბა ზღვარს იბეჭდება მესიჯი
                    self.vat_registered = True
            except ValueError:
                print("Invalid date format or turnover amount.")

            choice = input("Do you want to register another turnover? (y/n): ")
            if choice.lower() != 'y':
                break

        self.save_to_csv(f"{self.username}_turnover_records.csv")

    def load_turnover_records(self):
        filename = f"{self.username}_turnover_records.csv"
        if os.path.exists(filename):
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                self.turnover_records = {datetime.strptime(row['Date'], "%Y-%m-%d").date(): float(row['Turnover']) for row in reader}
        else:
            self.turnover_records = {}

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Date', 'Turnover']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for date, turnover in self.turnover_records.items():
                writer.writerow({'Date': date.strftime("%Y-%m-%d"), 'Turnover': turnover})



user_reg = User(None, None)
user_reg.register()