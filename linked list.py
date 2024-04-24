Linked list construction

class Box:
   def __init__(self, data):
       self.data = data
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   return head


def printLinkedList(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
      
n = int(input())
l = list(map(int, input().split()))
head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLinkedList(head)




Inserting a node at tail of linked list

def insertNodeAtTail(head, data):
   newNode = SinglyLinkedListNode(data)
   if head == None:
       return newNode
  
   tail = head
   while tail.next != None:
       tail = tail.next
   tail.next = newNode
   return head


Inserting a node at head of linked list

def insertNodeAtHead(llist, data):
   newNode = SinglyLinkedListNode(data)
   if llist == None:
       return newNode
   newNode.next = llist
   return newNode


Insert a node at specific position in a linked list

def insertNodeAtPosition(llist, data, position):
   newNode = SinglyLinkedListNode(data)
   index = 0
   curr = llist
   prev = None
  
   while index != position:
       prev = curr
       curr = curr.next
       index += 1
      
   if prev == None:
       newNode.next = llist
       return newNode
  
   newNode.next = prev.next
   prev.next = newNode
   return llist



Deleting tail node in singly linked list

class Box:
   def __init__(self, data):
       self.data = data
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
      
def deleteTailNode(head):
   if head == None or head.next == None:
       return None
  
   prev = None
   curr = head
   while curr.next != None:
       prev = curr
       curr = curr.next
      
   prev.next = None
   return head
  
n = int(input())
l = list(map(int, input().split()))


head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)


head = deleteTailNode(head)


printLeftToRight(head)



Deleting head node in singly linked list

class Box:
   def __init__(self, data):
       self.data = data
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
      
def deleteHeadNode(head):
   if head == None or head.next == None:
       return None
  
   head = head.next
   return head
  
n = int(input())
l = list(map(int, input().split()))


head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)


head = deleteHeadNode(head)


printLeftToRight(head)

Delete a node at specific position in singly linked list

class Box:
   def __init__(self, data):
       self.data = data
       self.next = None


      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = Box(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
      
def deleteAtSpecificPosition(head, position):
   currInd = 1
   curr = head
   prev = None
  
   while currInd != position:
       currInd += 1
       prev = curr
       curr = curr.next
      
   if prev == None:
       head = head.next
       head.prev = None
       return head
  
   prev.next = curr.next
   return head
  
n = int(input())
l = list(map(int, input().split()))
position = int(input())


head = None
for ele in l:
   head = insertAtEnd(head, ele)
  
printLeftToRight(head)


head = deleteAtSpecificPosition(head, position)


printLeftToRight(head)



