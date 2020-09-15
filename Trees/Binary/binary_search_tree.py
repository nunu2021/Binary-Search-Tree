# This is a single node in a Binary Tree
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left=None
# This gives the individual binary tree
class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root) # root is the top most node in a binary tree

    def print_tree(self, traversal_type): # organizes the different Depth-first search traversals
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type unsupported")
            return False


    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start: # check whether the root n=node is null or not
            traversal += (str(start.value)+ "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""

        if start:  # check whether the root n=node is null or not

            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)

        return traversal

    def postorder_print(self, start, traversal):
        """Left  -> Right-> Root"""

        if start:  # check whether the root n=node is null or not

            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")


        return traversal



#         1
#       /   \
#      /     \
#     2       3
#    / \     / \
#   4   5   6   7
#                \
#                 8



tree = BinaryTree(1)
tree.root.left = Node(2)# defining the left child
tree.root.right= Node(3) # defining the right child
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

# How to TRAVERSE = how to move through the list
# 1. depth first search
#     -pre order
#     -in order
#     -post order

# PRE ORDER:
# 1. check if node is null, if not:
# 2. Root, Left, right order
# 3. Do this recursively

# IN ORDER:
# 1. check if node is null, if not:
# 2. Left, Root, Right order
# 3. Do this recursively

print(tree.print_tree("preorder")) # 1-2-4-5-3-6-7-8-
print(tree.print_tree("inorder")) #4-2-5-1-6-3-7-8-
print(tree.print_tree("postorder")) #4-5-2-6-8-7-3-1-


