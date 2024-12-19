# this is class for the node :what is node -> it is data structure that contain data and value as data and next

class node:
    #make a function "init" is a predefined in py pass the argument self it will do " take the parameter and make bond with calss structure" 
    def __init__(self,v_data=None ,v_next=None):# default the data and next is None
            
            self.data = v_data
            self.next = v_next

class linklist:
      def __init__(self):
            self.head = None

if __name__ == '__main__':
      pass

        