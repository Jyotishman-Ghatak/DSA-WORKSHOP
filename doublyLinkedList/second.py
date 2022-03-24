# Create the node class
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None


# Create the doubly linked list class
class doubly_linked_list:
   def __init__(self):
      self.head = None

#  method to add elements at the begining
   def insertAtBegin(self, NewVal):
      NewNode=Node(NewVal)
      if(self.head is None):
         self.head= NewNode
         return
      temp=self.head
      temp.prev=NewNode
      NewNode.next=temp
      self.head=NewNode
      return

      # NewNode = Node(NewVal)
      # if(self.head is None):
      #     self.head=NewNode
      #     return

      # NewNode.next = self.head
      # self.head.prev=NewNode
      # self.head = NewNode

# method to add elements at the end
   def insertAtEnd(self, NewVal):
      NewNode=Node(NewVal)
      if self.head is None:
         self.head=NewNode
         return
      temp=self.head
      while(temp.next is not None):
         temp=temp.next
      temp.next=NewNode
      NewNode.prev=temp
      return










      # NewNode = Node(NewVal)
      # NewNode.next = None
      # if self.head is None:
      #    self.head = NewNode
      #    return
      # last = self.head
      # while (last.next is not None):
      #    last = last.next
      # last.next = NewNode
      # NewNode.prev = last
      # return
    

   def deleteAtBegin(self):

       if self.head is None:
           return
       temp=self.head
       self.head=self.head.next
       temp.next=None
       self.head.prev=None
       return




      #  temp=self.head
      #  self.head=self.head.next
      #  self.head.prev=None
      #  return
   def deleteAtEnd(self):
      if self.head is None:
         return
      temp=self.head
      while(temp.next.next is not None):
         temp=temp.next
      temp.next.prev=None
      temp.next=None
      return
# Define the method to print
   def listprint(self, node):
      while (node is not None):
         print(node.data,end=" "),
         last = node
         node = node.next

dllist = doubly_linked_list()
dllist.insertAtBegin(12)       
dllist.insertAtBegin(8)
dllist.insertAtEnd(7)
#dllist.deleteAtBegin()
dllist.deleteAtEnd()
# dllist.insertAtEnd(9)

# dllist.insertAtBegin(62)       # 62 8 12 9 45 
# dllist.insertAtEnd(45)

dllist.listprint(dllist.head)