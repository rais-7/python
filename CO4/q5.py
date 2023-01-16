class Publisher:
    def __init__(self, name):
        self.name = name
class Book(Publisher):
    def __init__(self, name, title, author):
        Publisher.__init__(self, name)
        self.title = title
        self.author = author
class Python(Book):
    def __init__(self, name, title, author, price, no_pages):
        Book.__init__(self, name, title, author)
        self.price = price
        self.no_pages = no_pages
    def display(self):
        print(self.name, self.title, self.author, self.price, self.no_pages)
i = 0
while(i != 1):
    ch = int(input("ENTER 1:Insert 2:Display 3:Exit :"))
    if(ch == 1):
        p1 = Python(input("ENTER PUBLISHER :"), input("ENTER TITLE :"), input("ENTER AUTHOR :"), int(input("ENTER PRICE :")), int(input("ENTER NUMBER OF PAGES :")))
    elif ch==2:
        p1.display()
    elif ch == 3:
        i = 1
    else:
        print("Wrong choice!")
            