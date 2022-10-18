class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, data):
        self.root = BinarySearchTree._insert(self.root,data)
    def _insert(root, data):
        if root == None:
            return Node(data)
            
        else:
            if data < root.data:
                root.left = BinarySearchTree._insert(root.left,data)
            else:
                root.right = BinarySearchTree._insert(root.right,data)
            return root
    def findsuccessor(self, root):
        minimum = root.data
        while root.left != None:
            minimum = root.left.data
            root = root.left
        return minimum
    def Delete(self, root, data):
        if isExit(root,data) == False:
            print("Error! Not Found DATA")
        self.root = self.delete(root, data)
    def delete(self, root, data):
        if root == None:
            return root
        if data == root.data:
            
            if root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
            else:
                root.data = self.findsuccessor(root.right)
                root.right = self.delete(root.right, root.data)
        elif data < root.data:
            root.left = self.delete(root.left, data)
        else:
            root.right = self.delete(root.right, data)
        return root
def isExit(root,data):
    if root == None:
        return False
    if root.data == data:
        return True
    if data < root.data:
        return isExit(root.left, data)
    else:
        return isExit(root.right, data)
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in range(len(data)):
    data[i] = data[i].split()

for i in range(len(data)):
    if data[i][0]=='i':
        print("insert "+data[i][1])
        tree.insert(int(data[i][1]))
    else :
        print("delete "+data[i][1])
        tree.Delete(tree.root,int(data[i][1]))
    printTree90(tree.root)