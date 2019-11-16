class Numbers:

    def __init__(self, value):
        self.value = value

    def Accept(self):
        self.value = int(input("Enter number:"))
        return self.value

    def chkPrime(self, value):
        for x in range(2, value):
            if ((value % x) == 0):
                return 0

    def chkPerfect(self, value):
        sum = 0
        for x in range(1, value):
            if ((value % x) == 0):
                sum = sum + x
        return sum

    def Factors(self, value):
        arr = list()
        for x in range(1, value):
            if ((value % x) == 0):
                arr.append(x)
        return arr

     def SumFactor(self, arr):
        sumFact = 0
        for x in range(0, len(arr)):
            sumFact = sumFact + arr[x]
        return sumFact

def main():
    Obj1 = Numbers(0);
    acceptedValue = Obj1.Accept()
    primeRes = Obj1.chkPrime(acceptedValue)
    if (primeRes == 0):
        print("number is not prime")
    else:
        print("number is prime", )

    perfectRes = Obj1.chkPerfect(0)
    if (perfectRes == acceptedValue):
        print("number is perfect")
    else:
        print("number is not perfect")

    factorRes = Obj1.Factors(acceptedValue)
    print("Factors of number are:", factorRes)

    additionOfFactor = Obj1.SumFactor(factorRes)
    print("Addition of Factors of number is:", additionOfFactor)


if __name__ == "__main__":
    main();
