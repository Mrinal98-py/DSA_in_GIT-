class node:#creating the node
    def __init__(self,data=None,next=None): #basic function in which the data and next will be pass 
        self.data=data  #putting data value 
        self.next=next  #putting address value

class linklist: #linklist class/structure is created
    def __init__(self): #function to pass the 1st value in the node (self.head = None) 
        self.head = None #head value is default null so we can store the value in the | self.head = None

    def insertin_begining(self,data):
        newnode = node(data)
    