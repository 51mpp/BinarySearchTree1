




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
            return root
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def X3(self, node,x, level = 0):
        if node != None:
            self.X3(node.right,x, level + 1)
            if node.data > x:
                node.data = node.data*3
            self.X3(node.left,x, level + 1)

T = BST()   
inp = list(input("Enter Input : ").split("/"))


p = list(map(int,inp[0].split()))

for i in p:
    root = T.insert(i)

T.printTree(T.root)
print("--------------------------------------------------")
T.X3(T.root,int(inp[1]))
T.printTree(T.root)