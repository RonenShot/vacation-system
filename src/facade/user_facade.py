from src.logic.user_logic import UserLogic
import re
import datetime
class UserFacade:
    def __init__(self):
        self.params = []
        self.UserLogic = UserLogic()
    def getUserName(self):
        valid = False
        while not valid:
            check = True
            name = input("Please enter your first name: ")
            if len(name)<=1:
                check = False
            for ch in name:
                if ch.isalpha() == False:
                    check = False
            valid = check
            if not valid:
                print("Your name can only consist alphbetic letters and at least two chars")
            print("\n")
            
    def emailcheck(self):
      Email = input("Enter your email\n")
      regex = r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
      while True:
        if re.fullmatch(regex, Email):  # Check if the email matches the pattern
            break
        print("Your email is not correct.\n")
        Email = input("Enter your email again\n")
        
    def password_check(self):
      while True:
        password = input("Enter your password\n")
        upperCase = False
        number = False
        for ch in password:
            if ch.isupper():  
                upperCase = True
            elif ch.isdigit():  
                number = True
        if upperCase and number and len(password) > 5:
            break  
        else:
            print("Password is invalid. It must contain at least one uppercase letter, one number, and be longer than 5 characters.")
            
    def date_of_birth_check(self):
      cur_date = datetime.date.today()  
    
      while True:
        try:
            
            birthday_input = input("Enter your birthday (YYYY-MM-DD):\n")
            birthday = datetime.datetime.strptime(birthday_input, "%Y-%m-%d").date()  
            
            
            if birthday <= cur_date:
                print("Birthday is valid.")
                break  
            else:
                print("Your birthday cannot be in the future. Please enter a valid date.")
        
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
            
    def vacation_title(self):
      title  = input("enter a title for your vacation")
      while True:
        if title is not None:
            break
        
        
        
                    
                    
                    
if __name__ == "__main__":
    uf = UserFacade()
    
    
    uf.date_of_birth_check()