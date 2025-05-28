class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Pile:
    def __init__(self):
        self.top= None



    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
        print(f"Added : {data}")


    def pop(self):
        if self.top is None:
            print("The pile es none, not have nothing to deleted")
            return None
        
        removed_node=self.top
        self.top=self.top.next
        print(f"Removed : {removed_node.data}")
        return removed_node.data
    
    def show(self):
        current= self.top
        print(f"Content of the pile: ")
        while current:
            print(current.data, end="---)")
            current= current.next
        print("None(end os the pile)")


pile= Pile()
pile.push("Motorcycle")
pile.push("Car")
pile.push("Bicycle")
pile.show()

pile.pop()
pile.show()