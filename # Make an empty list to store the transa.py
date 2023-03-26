# Make an empty list to store the transactions

def add_transaction():
    # Prompt the user for the transaction type income or expense and then the amount
    transaction_t = input("Enter transaction type (income or expense): ")
    amount = float(input("Enter amount: "))

    # Add transaction to the list
    transactions.append((transaction_t, amount))

    # Print the confirmation message
    print("Transaction added.")

