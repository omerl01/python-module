

accounts = [
    {
    "name": "Omer", "account_id": 100, "balance": 50000, "pin": 1234
    },
                     {
    "name": "Daniel", "account_id": 200, "balance": 50000, "pin": 2345
    },                  
]

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123456"

def find_account(account_id):
    for account in accounts:
        if account["account_id"] == account_id:
            return account
    return None


user_pin_input = int(input("pass here your pin ")
                     )
def verify_pin(account, user_pin):
    is_pin_correct =  user_pin == account["pin"]
    return is_pin_correct

def deposit():
    #deposit logic
    pass

def withdraw():
    #withdrawc logic
    pass

def show_balance():
    pass

def create_account():
    pass

def show_all_accounts():
    pass

def admin_login():
    username = input("username: ")
    password = input("password: ")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    print("access denied")