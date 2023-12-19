class BankAccount():

    def __init__(self):
        self.amount = 0.0
        import random
        self.number = str(random.randint(1,9)) + str(random.randint(0,9)) + " "

        for i in range(24):
            if (i+1)%4:
                self.number += str(random.randint(0,9))
            else:
                self.number += str(random.randint(0,9)) + " "

    def saldo(self):
        print(f"{self.amount} PLN")

    def deposit(self, money):
        self.amount += money
    
    def withdraw(self, money):
        if self.amount > money:
            self.amount -= money
        else:
            print("Insufficient funds!")        

account1 = BankAccount()
account1.saldo()
account1.deposit(25.30)
account1.saldo()
account1.withdraw(31.70)
account1.saldo()
account1.withdraw(14)
account1.saldo()
