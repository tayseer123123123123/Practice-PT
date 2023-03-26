# Make an empty list to store the transactions

def add_transaction():
    # Prompt the user for the transaction type income or expense and then the amount
    transaction_t = input("Enter transaction type (income or expense): ")
    amount = float(input("Enter amount: "))

    # Add transaction to the list
    transactions.append((transaction_t, amount))

    # Print the confirmation message
    print("Transaction added.")

#Function for calculating the user's total income/expenses
def calculate_total():
    total_income = 0
    total_expenses = 0

    # Iterate through the transactions - update the totals accordingly
    for transaction in transactions:
        if transaction[0] == "Income":
            total_income += transaction[1]
        elif transaction[0] == "Expense":
            total_expenses += transaction[1]