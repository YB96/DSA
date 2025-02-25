class TreeNode:
    def __init__(self, data, childern = []):
        self.data = data
        self.childern = childern

    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.childern:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, TreeNode):
        self.childern.append(TreeNode)

tree = TreeNode("Drinks", [])
cold = TreeNode("COLD", [])
hot = TreeNode("HOT", [])
tree.add_child(cold)
tree.add_child(hot)
print(tree)
cola = TreeNode("COLA", [])
fanta = TreeNode("FANTA", [])
tea = TreeNode("TEA", [])
coffee = TreeNode("COFFEE", [])
cold.add_child(cola)
cold.add_child(fanta)
hot.add_child(coffee)
hot.add_child(tea)
print(tree)