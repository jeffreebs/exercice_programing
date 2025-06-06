def bubble_sort_num(list1):
    l=len(list1)
    for n in range (l):
        swapped= False                                  #En el peor de los casos este codigo es de tipo O(n^2) por poseer dos ciclos anidados


        for x in range (0,l-n-1):
            if list[x]>list[x+1]:
                list[x],list[x+1]=list[x+1],list[x]     #En el mejor de los casos sería O(n) gracias a la lista ya ordenada
                swapped= True


        if not swapped:
            break
    return list1


num= [1,2,3,4,5]
sort=bubble_sort_num(num)
print(sort)


#_______________________________________________________________________________________________________________________________________________________________________________________________________________________


def bubble_sort_num(list):
    l=len(list)
    for n in range (l):
        for x in range (l-1,n,-1):
            if list[x]<list[x-1]:                       #Este en ambos casos es de tipo O(n^2) ya que contiene ciclos aninados
                list[x],list[x-1]=list[x-1],list[x]
    return list


num= [1,2,3,4,5]
sort=bubble_sort_num(num)
print(sort)


#______________________________________________________________________________________________________________________________________________________________________________________________________________________

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
            self.head = new_node                                        #En el mejor de los casos puede ser de tipo O(n) por el hecho de manejar listas ordenadas
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
                                                                        #En el peor de los casos puede ser O(n^2) porque contiene ciclos anidados y deben de reordenar la lista

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
