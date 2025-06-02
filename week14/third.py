class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right= None


class Binary_tree:
    def __init__(self):
        self.root=None


    def insert(self,value):
        new=Node(value)

        if self.root is None:
            self.root=new
        else:
            self.insert_another(self.root, new)

    def insert_another(self,current,new):
        if new.value < current.value:
            if current.left is None:
                current.left = new
            else:
                self.insert_another(current.left, new)
        else:
            if current.right is None:
                current.right= new
            else:
                self.insert_another(current.right, new)


    
    def paint(self):
        if self.root is None:
            print ("The Binary Tree is empty, Nothing to print")
            return
        
        
        print("Binary Tree (in_order):")
        self.in_order(self.root)
        print("None")


    def in_order(self,node):
        if node:
            self.in_order(node.left)

            print (node.value, end="----->")
            self.in_order(node.right)



tree=Binary_tree()

tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(3)
tree.insert(14)

tree.paint()