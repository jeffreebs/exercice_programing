class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
        self.prev= None


class Route:
    def __init__(self):
        self.right=None
        self.left=None


    def push_left(self,data):
        new_node=Node(data)


        if self.left is None and self.right is None:
            self.left= self.right=new_node
        else:
            new_node.next=self.left
            self.left.prev=new_node
            self.left = new_node

    
    def push_right(self,data):
        new_node=Node(data)


        if self.right is None and self.left is None:
            self.right= self.left=new_node
        else:
            self.right.next=new_node
            new_node.prev = self.right
            self.right = new_node



    def pop_left(self):
        if self.left is None:
            print("Route is None")
            return None
        if self.left== self.right:
            data= self.left.data
            self.left=self.right = None
            return data
        else:
            data = self.left.data
            self.left=self.left.next
            self.left.prev = None
            return data
        

    def pop_right(self):
        if self.right is None:
            print("Route is None")
            return None
        
        data=self.right.data

        if self.right==self.left:
            self.right=self.left= None

        else:
            self.right=self.right.prev
            self.right.nex = None

            return data
        

        if self.right== self.left:
            data= self.right.data
            self.right=self.left = None
            return data
        

        else:
            data = self.right.data
            self.right=self.right.prev
            self.right.next = None
            return data
        

    def show(self):
        current=self.left
        print("Route content")
        while current:
            print(current.data, end="<---->")
            current=current.next
        print("None")

if __name__ == "__main__":

    demo= Route()
    demo.push_left("Juan")
    demo.push_right("Matías")
    demo.push_left("Josue")
    demo.push_right("Chus")


    demo.show()

    demo.pop_left()
    demo.show()


    demo.pop_right()
    demo.show()

