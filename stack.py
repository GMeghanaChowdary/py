Stack-Construction (Linked list based implementation)



class Node:
   def __init__(self, data):
       self.data = data
       self.next = None
      
      
def push(top, val):
   print(val, "inserted")
   newNode = Node(val)
   newNode.next = top
   return newNode


def topValue(top):
   if top == None:
       print("Stack is empty")
       return
   print(top.data)
  
def pop(top):
   if top == None:
       print("Stack is empty")
       return None
   print(top.data)
   temp = top.next
   top.next = None
   return temp


def printStack(top):
   if top == None:
       print("Stack is empty")
       return
  
   curr = top
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printStackEmpty(top):
   if top == None:
       print("Stack is empty")
   else:
       print("Stack is not empty")
  




top = None
n = int(input().strip())
while n > 0:
  word = list(map(int, input().split()))
  l = word[0]
  if l == 1:
      num = word[1]
      top = push(top, num)
  elif l == 2:
      topValue(top)
  elif l == 3:
      top = pop(top)
  elif l == 4:
      printStack(top)
  else:
      printStackEmpty(top)
  n -= 1


Stack-Construction (Array based implementation)

stack = []
n = int(input().strip())
while n > 0:
   word = list(map(int, input().split()))
   l = word[0]
   if l == 1:
       num = word[1]
       stack.insert(0, num)
       print(num, "inserted")
   elif l == 2:
       if len(stack) == 0:
           print("Stack is empty")
       else:
           print(stack[0])
   elif l == 3:
       if len(stack) == 0:
           print("Stack is empty")
       else:
           print(stack[0])
           stack.pop(0)
   elif l == 4:
       if len(stack) == 0:
           print("Stack is empty")
       else:
           for ele in stack:
               print(ele, end = " ")
           print()
   else:
       if len(stack) == 0:
           print("Stack is empty")
       else:
           print("Stack is not empty")
      
   n -= 1
