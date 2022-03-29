# Create the node class
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None


# Create the doubly linked list class
class stack:
   def __init__(self):
      self.top = None
      

#  method to add elements at the begining
   def push(self, NewVal):
    
      NewNode= Node(NewVal)
      if(self.top is None):
          self.top=NewNode
          return
      
      NewNode.next=self.top
      self.top=NewNode
      
    
   def pop(self):
       if self.top is None:
           return

       temp=self.top
       self.top=self.top.next
       temp.next=None
       return

   def printStack(self, node):
      while (node is not None):
         print(node.data,end=" "),
         last = node
         node = node.next

   def checkBP(self,st):
       for i in range(0,len(st)):
           if(self.top is None):
               self.push(st[i])
           else:
               if((st[i]=="}" and self.top.data=="{" ) or (st[i]==")" and self.top.data=="(") or (st[i]==']' and self.top.data=='[')):
                   self.pop()
               else:
                   self.push(st[i])
        
       if(self.top is None):
           return "Yes"
       else:
           return "No"






    #    for i in range(0,len(st)):
    #        if(self.top is None):
    #            self.push(st[i])
    #        else:
    #            if((st[i]==")" and self.top.data=="(") or (st[i]=="}" and self.top.data=="{") or (st[i]=="]" and self.top.data=="[") ):
    #                self.pop()
    #            else:
    #                self.push(st[i])
    #    if(self.top is None):
    #        return "Yes"
    #    else:
    #        return "No"
               

       

stac = stack()
print(stac.checkBP('[(]('))        #{}{}[]][]


stac.printStack(stac.top)