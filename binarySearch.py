class getNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.mid = None
 

def hasPath(root, arr, x):
    if (not root):
        return False

    arr.append(root.data)    
     
    if (root.data == x):    
        return True
     
    if (hasPath(root.left, arr, x) or hasPath(root.right, arr, x) or hasPath(root.mid, arr, x)):
        return True
       
    arr.pop(-1)
    return False
 

def printPath(root, x):
     
    arr = []
     
    if (hasPath(root, arr, x)):
        for i in range(len(arr) - 1):
            print(arr[i], end = "->")
        print(arr[len(arr) - 1])

    else:
        print("No Path")
 

# if __name__ == '__main__':
#
#     # binary tree formation
#     root = getNode(0)
#     root.left = getNode(1)
#     root.right = getNode(2)
#     root.left.left = getNode(3)
#     root.left.right = getNode(4)
#     root.right.left = getNode(5)
#     root.right.right = getNode(6)
#
#     printPath(root, 6)
     
