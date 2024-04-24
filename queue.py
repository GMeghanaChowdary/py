Queue-Construction (Linked list based implementation)

class Node:
   def __init__(self, data):
       self.data = data
       self.next = None
      
def enQueue(head, val):
   print(val, "inserted")
   newNode = Node(val)
   if head == None:
       return newNode
  
   tail = head
   while tail.next != None:
       tail = tail.next
   tail.next = newNode
   return head


def deQueue(head):
   if head == None:
       print("Queue is empty")
       return None
  
   temp = head.next
   print(head.data)
   head.next = None
   return temp
  
def frontValue(head):
   if head == None:
       print("Queue is empty")
       return
   print(head.data)
  
def printQueue(head):
   if head == None:
       print("Queue is empty")
       return
  
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printIsQEmpty(head):
   if head == None:
       print("Queue is empty")
   else:
       print("Queue is not empty")


head = None
n = int(input().strip())
while n > 0:
  word = list(map(int, input().split()))
  l = word[0]
  if l == 1:
      num = word[1]
      head = enQueue(head, num)
  elif l == 2:
      frontValue(head)
  elif l == 3:
      head = deQueue(head)
  elif l == 4:
      printQueue(head)
  else:
      printIsQEmpty(head)
         
    
  n -= 1



Queue-Construction (Array based implementation)

Q = []
n = int(input().strip())
while n > 0:
   word = list(map(int, input().split()))
   l = word[0]
   if l == 1:
       num = word[1]
       Q.append(num)
       print(num, "inserted")
   elif l == 2:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           print(Q[0])
   elif l == 3:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           print(Q[0])
           Q.pop(0)
   elif l == 4:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           for ele in Q:
               print(ele, end = " ")
           print()
   else:
       if len(Q) == 0:
           print("Queue is empty")
       else:
           print("Queue is not empty")
      
   n -= 1


