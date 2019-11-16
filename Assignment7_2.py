class BankAccount():
    ROI = 10.5

    def __init__(self,name,amount):
        self.name = name;
        self.amount = amount;

    def Deposit(self, value):
        self.amount = self.amount + value;


    def Withdraw(self, value):
        self.amount = self.amount - value;

    def Accept(self):
        self.name = (input("Enter name:"))
        self.amount = int(input("Enter amount:"))
        return self.name, self.amount

    def Display(self, name, amount):
            print("Name: ", self.name)
            print("Amount: ", self.amount)


def main():
    Obj1 = BankAccount(0,0)
    Obj1.Accept()

    Obj1.Deposit(500)
    print("Inside Deposit")
    print(Obj1.Display(Obj1.name,Obj1.amount))

    print("Inside withdraw")
    Obj1.Withdraw(500)
    print(Obj1.Display(Obj1.name, Obj1.amount))

    Obj2 = BankAccount(0,0)
    Obj2.Accept()

    print("Inside Deposit")
    Obj2.Deposit(500)
    print(Obj2.Display(Obj2.name,Obj2.amount))

    print("Inside withdraw")
    Obj2.Withdraw(500)
    print(Obj2.Display(Obj2.name, Obj2.amount))


if __name__ == "__main__":
    main();
