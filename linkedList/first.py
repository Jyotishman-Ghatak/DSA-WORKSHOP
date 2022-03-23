# Create the node class
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None


# Create the doubly linked list class
class linked_list:
   def __init__(self):
      self.head = None

#  method to add elements at the begining
   def insertAtBegin(self, NewVal):
      
      NewNode= Node(NewVal)
      if(self.head is None):
          self.head=NewNode
          return
      
      NewNode.next=self.head
      self.head=NewNode
      
      
      
      
      
    #   NewNode = Node(NewVal)
    #   if(self.head is None):
    #       self.head=NewNode
    #       return

    #   NewNode.next = self.head
    #   self.head = NewNode

# method to add elements at the end
   def insertAtEnd(self, NewVal):
       NewNode=Node(NewVal)
       if self.head is None:
           self.head = NewNode
           return

       temp=self.head
       while(temp.next is not None):
           temp=temp.next
       temp.next=NewNode
       return



    #   last = self.head
    #   while (last.next is not None):
    #      last = last.next
    #   last.next = NewNode
    #   return
    

   def deleteAtBegin(self):
       if self.head is None:
           return

       temp=self.head
       self.head=self.head.next
       return

   def deleteAtEnd(self):
       if self.head is None:
           return
       temp=self.head
       while(temp.next.next is not None):
           temp=temp.next
       temp.next=None
       return

# Define the method to print
   def listprint(self, node):
      while (node is not None):
         print(node.data,end=" "),
         last = node
         node = node.next

llist = linked_list()
llist.insertAtBegin(12)     
llist.insertAtBegin(2)
llist.insertAtBegin(3)  
llist.insertAtEnd(9)
# llist.insertAtBegin(8)
# llist.insertAtBegin(62)       
# llist.insertAtEnd(45)
#llist.deleteAtEnd()

llist.listprint(llist.head)