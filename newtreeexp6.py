class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = TreeNode(val)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = TreeNode(val)
                        break
                    else:
                        curr = curr.right
    
    def get_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.get_height(node.left)
            right_height = self.get_height(node.right)
            return max(left_height, right_height) + 1
    
    def delete(self, val):
        self.root = self._delete_node(self.root, val)
    
    def _delete_node(self, node, val):
        if node is None:
            return node
        elif val < node.val:
            node.left = self._delete_node(node.left, val)
        elif val > node.val:
            node.right = self._delete_node(node.right, val)
        else:
            # Case 1: No child
            if node.left is None and node.right is None:
                node = None
            # Case 2: One child
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            # Case 3: Two children
            else:
                temp = self._get_min_node(node.right)
                node.val = temp.val
                node.right = self._delete_node(node.right, temp.val)
        return node
    
    def _get_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def is_balanced(self):
        return self._check_balanced(self.root) != -1
    
    def _check_balanced(self, node):
        if node is None:
            return 0
        left_height = self._check_balanced(node.left)
        if left_height == -1:
            return -1
        right_height = self._check_balanced(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1


# Construct the binary search tree
bst = BinarySearchTree()
bst_values = [12, 35, 14, 97, 36, 65, 89]
for val in bst_values:
    bst.insert(val)

# Insert new element
roll_number = 8 # replace with your last two digits of your roll number
bst.insert(roll_number)

# Get the height of the binary search tree
height = bst.get_height(bst.root)
print("Height of the BST:", height)

# Delete an element from the BST
bst.delete(roll_number)

# Check if the BST is balanced or not
if bst.is_balanced():
    print("The BST is balanced")
    bst._check_balanced(bst.root)
else:
    print("The BST is not balanced")
    bst._check_balanced(bst.root)


