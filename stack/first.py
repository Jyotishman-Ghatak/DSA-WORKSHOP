# Create the node class
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None


# Create the doubly linked list class
class stack:
   def __init__(self,cap):
      self.top = None
      self.size=0
      self.capacity=cap

#  method to add elements at the begining
   def push(self, NewVal):
      
      NewNode= Node(NewVal)
      if(self.size+1>self.capacity):
         print("Stack Overflow")
         return
      if(self.top is None):
          self.top=NewNode
          self.size+=1
          return
      
      NewNode.next=self.top
      self.top=NewNode
      self.size+=1
    
   def pop(self):
       if self.top is None:
           print("Stack Underflow")
           return

       temp=self.top
       self.top=self.top.next
       self.size-=1
       return

   def printStack(self, node):
      while (node is not None):
         print(node.data,end=" "),
         last = node
         node = node.next

st = stack(4)
st.push(12)
st.push(19)  
st.pop()
st.pop()
st.pop()
#st.push(16)
#print(st.capacity)
#st.pop()
# st.push(12)

#st.pop()
# llist.insertAtBegin(8)
# llist.insertAtBegin(62)       
# llist.insertAtEnd(45)
#llist.deleteAtEnd()

st.printStack(st.top)