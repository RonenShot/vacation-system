from src.utils.dal import DAL

class UserLogic:
     def __init__(self):
        self.dal = DAL() 
     def __enter__(self):
        return self
     def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()
     def user_register(self , first_name , last_name , email , password , date_of_birth ,role_id):
            if self.find_user(email) == True:
                print("This user already exists.")
                return False
            
            query = """
            INSERT INTO vacationsdatabase.users 
            (first_name , last_name , email , password , date_of_birth ,role_id)
            VALUES 
            (%s, %s, %s, %s, %s , %s )
            """
            params = (first_name , last_name , email , password , date_of_birth , role_id)
            self.dal.insert(query, params)
            return True
     def find_user(self , email):
         try: 
             query = "SELECT * FROM vacationsdatabase.users where email = %s"
             params = (email,)
             result = self.dal.get_table(query , params)
             if result:
                 return True
             return False
         except Exception as err:
             print(f"There was an error: {err}")
             
     def login_user(self , email , password):
         if(self.find_user(email) == False):
             print("This user doesn't exists")
             return False
         query = "Select * from vacationsdatabase.users where email = %s and password = %s"
         params = (email,password)
         result = self.dal.get_table(query , params)
         if result:
             print("loged in")
         else: 
             print("Wrong password")  
     
        
if __name__=="__main__":
    ul = UserLogic()
    #ul.user_register("bob" ,"taylor" ,"bob.taylor@example.com" , "hashed_password_4" , "1980-07-24" , "1")
    ul.user_register("ronen" , "shotlender" , "skmvx123@gmail.com" , "123456" , "2006-05-08" , "1")

        
    
   