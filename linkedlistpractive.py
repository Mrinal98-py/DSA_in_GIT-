class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedlist:
    def linkedlistconst(self, arr):
        self.head = Node(arr[0])
        curr = self.head
        for i in range(1,len(arr)):
            curr.next = Node(arr[i])
            curr = curr.next
    
        print(self.head)
        return self.head


if __name__ == '__main__':
    arr = [2,3,4,5]
    ob = 