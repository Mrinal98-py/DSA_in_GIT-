class library:
    def book_issue(self):
        self.id = int(input("ID"))
        self.name = str(input("NAME")) 
        self.issueDate = input("DATE I")
        self.returnDate = input ("RETURN DATE")

    def printinfo(self):
        print("id",self.id)
        print("name",self.name)
        print("issue",self.issueDate)
        print("return",self.returnDate)

        #class ready 

kiit = library()
KIMS = library()

print("KIIT LIBRARY")
kiit.book_issue()
kiit.printinfo()

print("KIMS LIBRARY")
KIMS.book_issue()
KIMS.printinfo()


    
