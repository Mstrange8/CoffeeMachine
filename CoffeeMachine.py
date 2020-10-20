

class CoffeeMachine:
    """CoffeeMachine is the parent class to the CashBox, Selector, Product classes."""
    def __init__(self):
        """Initializes classes and creates multiple objects for the Product class; one fore each type of coffee."""
        self.cashBox = CashBox()
        self.black = Product('black', ['cup', 'coffee', 'water'], 35)
        self.white = Product('white', ['cup', 'coffee', 'creamer', 'water'], 35)
        self.sweet = Product('sweet', ['cup', 'coffee', 'sugar', 'water'], 35)
        self.whitesweet = Product('whiteSweet', ['cup', 'coffee', 'sugar', 'creamer', 'water'], 35)
        self.bouillon = Product('bouillon', ['cup', 'bouillonPowder', 'water'], 25)
        self.selector = Selector(self.cashBox, [self.black, self.white, self.sweet, self.sweet, self.bouillon])

    def oneAction(self):
        """oneAction method continues to loop as long as True is returned. Once False is returned, the loop ends."""
        print("\n\tPRODUCT LIST: all 35 cents, except bouillon (25 cents)")
        print("\t1=black, 2=white, 3=sweet, 4=white & Sweet, 5=bouillon")
        print("\tsample commands: insert 25, select 1")

        command = input(">>> Your command: ")
        command = command.split()

        if command[0] == 'select':
            self.selector.select(int(command[1]))
        elif command[0] == 'insert':
            self.cashBox.deposit(int(command[1]))
        elif command[0] == 'cancel':
            self.cashBox.returnCoins()
        elif command[0] == 'quit':
            return False
        else:
            print("Invalid command")
        return True

    def totalCash(self):
        """Returns the total amount spent throughout the transaction."""
        return self.cashBox.total()


class CashBox:
    """The CashBox class controls the flow of money coming in and out of the machine."""
    def __init__(self):
        """credit is the amount currently in the machine. totalReceived is the amount the user has spent on coffee."""
        self.credit = 0
        self.totalReceived = 0

    def deposit(self, amount):
        """If amount is 5, 10, 25, or 50 cents then the amount is deposited as credit in the cash box."""
        if amount in [5, 10, 25, 50]:
            self.credit += amount
            print("Depositing " + str(amount) + " cents. You have " + str(self.credit) + " cents credit.")
        else:
            print("INPUT ERROR >>>")
            print("We only take half-dollars, quarters, dimes, and nickels. \nCoin(s) returned")

    def returnCoins(self):
        """Returns the amount of money currently in the cash box and set credit back to 0."""
        print("Returning " + str(self.credit) + " cents.")
        self.credit = 0

    def haveYou(self, amount):
        """Tests if user has enough credit for the desired product."""
        if self.credit >= amount:
            return True
        else:
            return False

    def deduct(self, amount):
        """Deducts the cost of the product from the credit and adds the cost of the products the the totalReceived."""
        self.credit -= amount
        self.totalReceived += amount

    def total(self):
        """returns the total amount spent on products."""
        return self.totalReceived


class Selector:
    """The Selector class makes calls to the CashBox and Products class based on the desired coffee."""
    def __init__(self, cashBox, product):
        """Initializes the arguments cashBox and products. products is a list of objects for the Product class."""
        self.cashBox = cashBox
        self.product = product

    def select(self, choiceIndex):
        """Performs an action based on what type of coffee is selected."""
        if choiceIndex in [1, 2, 3, 4, 5]:
            prod = self.product[choiceIndex - 1]
            if self.cashBox.haveYou(prod.getPrice()):
                self.cashBox.deduct(prod.getPrice())
                prod.make()
                self.cashBox.returnCoins()
            else:
                print("Sorry. Not enough money deposited.")
        else:
            print("Input Error")


class Product:
    """The Products class prints out the name and recipe based on the Products object that is called."""
    def __init__(self, product, recipe, price):
        """Initializes the arguments product, recipe, and recipe. recipe is a list of ingredients."""
        self.product = product
        self.ingredients = recipe
        self.price = price

    def getPrice(self):
        """Returns the price of the coffee."""
        return self.price

    def make(self):
        """Prints out the name and the recipe for the coffee."""
        print("Making {}".format(self.product))
        for a in self.ingredients:
            print("\tDispensing {}".format(a))


def main():
    """Runs the oneAction method in a while loop. Prints out the total cash spent throughout the transaction."""
    m = CoffeeMachine()
    while m.oneAction():
        pass
    total = m.totalCash()
    print(f"Total cash: ${total/100:.2f}")


if __name__ == '__main__':
    main()