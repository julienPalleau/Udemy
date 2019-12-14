class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Le compte est detenu par Monsieur : {self.owner}\nLa balance de ce compte est de {self.balance} euros"

    def Balance(self):
        return f"Votre balance est de {self.balance} euros"

    def Owner(self):
        return f"Le proprietaire du compte est Mr {self.owner}"

    def Deposit(self, deposit):
        self.deposit = deposit
        self.balance += self.deposit
        return f"Votre deposit de {self.deposit} euros est accepte \
            \nVotre nouvelle balance est de : {self.balance} euros"

    def Withdraw(self, withdraw):
        self.withdraw = withdraw
        if (self.withdraw < self.balance):
            self.balance -= self.withdraw
            return f"Votre retrait de {self.withdraw} euros est accepte \
                \nVotre nouvelle balance est de : {self.balance} euros"
        else:
            print(
                "Retrait impossible ! Le montant retire est superieur à la balance de votre compte !")


acct1 = Account('Julien', 1000)
print(acct1)
print("\n")
print(acct1.Owner())
print(acct1.Balance())
print("\n")
print(acct1.Deposit(100))
print("\n")
print(acct1.Withdraw(200))
print("\n")
print(acct1.Withdraw(1000))
