#https://www.geeksforgeeks.org/binary-tree-data-structure/
#https://www.freecodecamp.org/news/binary-search-tree-what-is-it/
#https://www.geeksforgeeks.org/types-of-binary-tree/

#Pre Order Traversal Using Linked List

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

newBT = TreeNode("Main - Drinks")
leftchild = TreeNode("Drinks L1 - Hot")
rightchild = TreeNode("Drinks R1 - Cold")
tea = TreeNode("Hot L11 - Tea")
coffee = TreeNode("Hot L12 - Coffee")
coca = TreeNode("Cold R11 - Coca Cola")

leftchild.leftchild = tea
leftchild.rightchild = coffee
rightchild.leftchild = coca
newBT.leftchild = leftchild
newBT.rightchild = rightchild


#Pre Order Traversal Using Linked List
#The Preorder traversal visits the nodes in the following order: [Root, Left, Right].
print("----PreOrder Traversal----")

def PreOrderTrav(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    PreOrderTrav(rootNode.leftchild)
    PreOrderTrav(rootNode.rightchild)

PreOrderTrav(newBT)

#InOrder Traversal Using Linked List
#The Inorder Traversal visits the nodes in the following order: [Left, Root, Right].
print("----InOrder Traversal----")

def InOrderTrav(rootNode):
    if not rootNode:
        return
    InOrderTrav(rootNode.leftchild)
    print(rootNode.data)
    InOrderTrav(rootNode.rightchild)

InOrderTrav(newBT)


#PostOrder Traversal Using Linked
#The Post Order Traversal visits the nodes in the following order: Left, Right, Root.
print("----PostOrder traversal----")

def PostOrderTrav(rootNode):
    if not rootNode:
        return
    PostOrderTrav(rootNode.leftchild)
    PostOrderTrav(rootNode.rightchild)
    print(rootNode.data)

PostOrderTrav(newBT)

#Level Order Traversal Using Linked List
#The main idea of level order traversal is to traverse all the nodes of a lower level before moving 
# to any of the nodes of a higher level.
print("----LevelOrder traversal----")

import QueueLinkedList as queue

def LevelOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
            
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)

LevelOrderTrav(newBT)

#Searching for a Node in Binary Tree (Linked List)


def seachBT(rootNode, rootValue):
    if not rootNode:
        return "The Binary Tree dosenot exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)


