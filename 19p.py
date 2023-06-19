class Queue:
  def _init_(self):
    self.items=[]
  def enqueue(self,item):
      self.items.append(item)
  def dequeue(self):
    if self.isEmpty():
       print("Queue is Empty cannot delete")
    else:
      item=self.items.pop(0)
      print("Deleted Item is:",items)
  def display(self):
    if self.isEmpty():
       print("Queue is Empty")
    else:
      print(self.items)
  def length(self):
   return len(self.item)
  def isEmpty(self):
   return len(self.items)==0
q = Queue()
while (True):
 print("1:Enqueue2:Dequeue3:Display4:Length5:Exit")
 choice=int(input("enter your choice:"))
 if choice==1:
    item=input("Enter the element:")
    q.enqueue(item)
 elif choice==2:
    q.dequeue()
 elif choice==3:
    q.display()
 elif choice==4:
    n=q.length()
    print("Lenght of the queue is",n)
 elif choice==5:
    break