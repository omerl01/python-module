def find_account(account_id):
    for account in accounts:
        if account["account_id"] == account_id:
            return account
    return None

def verify_pin(account, pin):
    return account["pin"] == pin