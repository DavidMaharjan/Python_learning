class Category:
    # Represents a budget category with a ledger for transactions
    def __init__(self, name):
        # Initialize category with a name and empty ledger
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Add a deposit to the ledger
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        # Attempt to withdraw amount if funds are available
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        # Return current balance by summing all ledger amounts
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        # Transfer amount to another category if funds are available
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        # Check if enough funds are available for a transaction
        return amount <= self.get_balance()

    def __str__(self):
        # Return a formatted string representation of the ledger
        # Title
        output = self.name.center(30, "*") + "\n"

        # Ledger entries
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:>7.2f}"
            output += f"{description}{amount}\n"

        # Total
        output += f"Total: {self.get_balance():.2f}"
        return output
def create_spend_chart(categories):
    # Print a spend chart showing percentage spent by each category
    print("Percentage spent by category")
    spendings = []
    total_spent = 0
    # Calculate total spent per category
    for category in categories:
        # Sum negative amounts (withdrawals) for each category
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spendings.append(spent)
        total_spent += spent

    # Calculate percentage spent for each category (rounded down to nearest 10)
    percentages = [int(spent / total_spent * 10) * 10 for spent in spendings]

    # Print chart lines for each percentage level
    for i in range(100, -1, -10):
        line = f"{i:>3} | "
        for percentage in percentages:
            line += "o  " if percentage >= i else "   "
        print(line)
    # Print separator line
    print("    " + "-" * (len(categories) * 3 + 1))

    # Print category names vertically
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        line = "     "
        for category in categories:
            line += f"{category.name[i] if i < len(category.name) else ' '}  "
        print(line)

 # Example usage and tests
if __name__ == "__main__":
    # Create categories
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")

    # Add transactions to Food
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food")
    food.transfer(50, entertainment)

    # Add transactions to Entertainment
    entertainment.deposit(100, "initial deposit")
    entertainment.withdraw(15, "movie ticket")

    # Add transactions to Business
    business.deposit(500, "initial deposit")
    business.withdraw(100, "office supplies")

    # Print category ledgers
    print(food)
    print()
    print(entertainment)
    print()
    print(business)
    print()
    # Print spend chart
    create_spend_chart([food, entertainment, business])

