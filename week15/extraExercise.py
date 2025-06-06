class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head = new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node


    def show(self):
        current=self.head
        while current:
            print(current.data,end="--->")
            current=current.next
        print("None")


    def bubble_sort(self):
        if not self.head:
            print("The list is empty, can not to order right now")
            return
        

        swapped=True
        while swapped:
            current=self.head
            swapped= False
            while current.next:
                if current.data > current.next.data:

                    current.data , current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    # def bubble_sort(self):
    #     if not self.head or not self.head.next:
    #         return

    #     swapped= True
    #     while swapped:
    #         swapped= False
    #         prev=None
    #         current = self.head


    #         while current and current.next:
    #             a= current
    #             b=current.next

    #             if a.data> b.data:
    #                 swapped= True

    #                 a.next = b.next
    #                 b.next = a

    #                 if prev:
    #                     prev.next =b
    #                 else:
    #                     self.head = b
                    

    #                 prev=b
    #                 current=a
    #             else:
    #                 prev = current
    #                 current = current.next


element=LinkedList()

element.append(7)
element.append(3)
element.append(9)
element.append(1)
element.append(5)


print("This is the list before to order:")
element.show()


element.bubble_sort()


print("This is the list before to order:")
element.show()

