def users_with_negative_balance(transactions):

    result=[]
    user_balances={}
    negative_users = set()

    for txn in transactions:
        user_id=txn["user_id"]
        amount=txn["amount"]


        if user_id not in user_balances:
            user_balances[user_id]=0
        user_balances[user_id]+=amount

        if user_balances[user_id]<0 and user_id not in negative_users:
            negative_users.add(user_id)
            result.append(user_id)
    return result


transactions = [
    {"user_id": 1, "amount": 500, "timestamp": "2025-01-01T10:00:00"},
    {"user_id": 2, "amount": 300, "timestamp": "2025-01-01T10:05:00"},
    {"user_id": 1, "amount": -700, "timestamp": "2025-01-01T10:10:00"},
    {"user_id": 3, "amount": 200, "timestamp": "2025-01-01T10:15:00"},
    {"user_id": 2, "amount": -350, "timestamp": "2025-01-01T10:20:00"},
    {"user_id": 3, "amount": -250, "timestamp": "2025-01-01T10:25:00"},
]


print(users_with_negative_balance(transactions))
