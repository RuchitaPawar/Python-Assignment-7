class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name  = Name
        self.Author = Author
        self.NoOfBooks = self.NoOfBooks + 1

    def Display(self):
        print("Book  Name",self.Name)
        print("Author Name", self.Author)
        print("Number of books",self.NoOfBooks)



def main():
    Obj1 = BookStore("LinuxSystemProgramming", "RobertLove")
    Obj1.Display()  # Linux System Programming by Robert Love. No of books : 1

    Obj2 = BookStore("CProgramming", "DennisRitchie")
    Obj2.Display()  # C Programming by Dennis Ritchie. No of books : 2


if __name__ == "__main__":
    main();