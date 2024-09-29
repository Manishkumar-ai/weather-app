import queue
queue=queue.PriorityQueue()
queue.put((3,"manish"))
queue.put((4,"pal pandi"))
queue.put((6,"Ruban"))
queue.put((1,"Tamil"))
queue.put((5,"Vignesh"))
queue.put((2,"Monesh"))
while True:
    choice=int(input("Enter the your choice:"))
    if choice==1:
        e=queue.get()
        print("Removed element:",e)
    elif choice==2:
        break
    else:
        print("Enter the correct choice")
