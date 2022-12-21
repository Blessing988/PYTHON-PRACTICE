
class Password(object):
    """
    A class used to represent the Password security system

    ...

    Class Atributes
    ---------------
    stored_values : dict
        a dictionary which contains the username as the key and password as the key

    Instance Attributes 
    -------------------
    username : str
        a string to be used as username for log in or sign up 
    passwword : a string to be used as passwword for log in or sign up

    Methods
    ----------------
    SignUp()
        Creates a new username or password if user wants to create a new account 
    
    check_length()
        Returns a bool to indicate whether the password is of the required length

    validate()
        Performs the overall checks to make sure the user can log in or Sign Up 
    """
    stored_values = {"Blessing": 'Kyem'}

    def __init__(self):
        self.username = input('\nEnter your username: \n')
        self.password = input('\nEnter your password: \n ')
    
    def signUp(self):
        """Creates a new username or password if user wants to create a new account 

        Results
        ------------
        Adds the username or password to `store_values` dictionary if it passes all the 
        necessary checks 
        """

        while True:
            if self.username in Password.stored_values.keys():
                print('\nUsername already exists')
                self.username = input('\nEnter a unique username: \n')
                continue
            elif len(self.username) < 3 :
                print('Username must be at least 3 or more characters')
                self.username = input('Enter a valid username: \n')
                continue
            elif self.username.isnumeric():
                print('Username can\'t only be numbers')
                self.username = input('Enter a valid username: \n')
                continue
            elif self.username not in Password.stored_values.keys():
                if ' ' in self.password:
                    print('\nInvalid password')
                    print('Password must not contain whitespaces\n')
                    self.password = input('\nEnter a valid password: \n')
                    continue
                elif self.check_length():
                    print('\nPassword you entered must have a minumum length of 7')
                    self.password = input('\nEnter a valid password: \n')
                    continue
            
            Password.stored_values[self.username] = self.password
            print('\nAccount created Sucessfully!\n')
            break
            
    def check_length(self):
        """Returns a bool to indicate whether the password is of the required length"""

        not_valid = True
        if len(self.password) >= 7:
            not_valid = False 
        return not_valid
    
    def validate(self):
        """Performs the overall checks to make sure the user can log in or Sign Up """

        no_of_failed_attempts = 0
        while no_of_failed_attempts <= 3:
            try:
                if Password.stored_values[self.username].lower() == self.password.lower():
                    print('\nLogin Successful')
                    quit()
            except KeyError:
                print('\nUsername does not exist')
                result = input('\nDo you want to create an account? \n').lower()
                if result == 'yes' :
                    new_user = Password()
                    new_user.signUp()
                    print('You can login now \n')
                    new_login = Password()
                    new_login.validate()
                    quit()
                
            print('Incorrect username or password')
            if ' ' in self.password:
                print('Password must not contain whitespaces')
            no_of_failed_attempts += 1 
            if no_of_failed_attempts == 3 :
                break
            self.username = input('\nEnter the correct username: \n')
            self.password = input('\nEnter the correct password: \n')


# Create an instance 
user = Password()
# Start validation 
user.validate()