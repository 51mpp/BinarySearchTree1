

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = BST._insert(self.root,data)
    def _insert(root, data):
        if root == None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._insert(root.left,data)
            else:
                root.right = BST._insert(root.right,data)
            x = root
            return root
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def preOrder(self,node):
        if node!= None:
            print(node.data,end="")
            self.preOrder(node.left)
            self.preOrder(node.right)
    def inOrder(self,node,level=0):
        if node!= None:
            if node.right !=None and node.left !=None: 
                print("(",end="")
            self.inOrder(node.left,level + 1)
            print(node.data,end="")
            self.inOrder(node.right, level + 1)
            if node.right !=None and node.left !=None: 
                print(")",end="")

class Stack:
    def __init__(self,List = None):
            if List == None:
                self.items = []
                self.size = 0
            else:
                self.items = List
                self.size = len(List)
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def sizes(self):
        return len(self.items)
    

T = BST()   
S = Stack()
inp = input("Enter Postfix : ")

for i in inp:
    if i == "+" or i ==  "-" or i ==  "*" or i ==  "/":
        b = Node(i)
        b.right = S.pop()
        b.left = S.pop()
        S.push(b)
    else:
        b = Node(i)
        S.push(b)
print("Tree :")
T.printTree(b)
print("--------------------------------------------------")
print("Infix : ",end="")
T.inOrder(b)
print()
print("Prefix : ",end="")
T.preOrder(b)
print()