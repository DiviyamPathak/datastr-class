import random

class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class FullBinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            self.size += 1
        else:
            q = [self.root]
            while q:
                curr = q.pop(0)
                if curr.left is None:
                    curr.left = TreeNode(val)
                    self.size += 1
                    break
                elif curr.right is None:
                    curr.right = TreeNode(val)
                    self.size += 1
                    break
                else:
                    q.append(curr.left)
                    q.append(curr.right)
    
    def find_min(self):
        if self.root is None:
            return None
        else:
            min_val = float('inf')
            q = [self.root]
            while q:
                curr = q.pop(0)
                if curr.val < min_val:
                    min_val = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            return min_val
    
    def find_max(self):
        if self.root is None:
            return None
        else:
            max_val = float('-inf')
            q = [self.root]
            while q:
                curr = q.pop(0)
                if curr.val > max_val:
                    max_val = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            return max_val
    
    def calculate_sum(self):
        if self.root is None:
            return None
        else:
            sum_val = 0
            q = [self.root]
            while q:
                curr = q.pop(0)
                sum_val += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            return sum_val
    
    def pre_order_traversal(self, node=None):
        if node is None:
            node = self.root
            return
        if node:
            print(node.val, end=' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    
    def post_order_traversal(self, node=None):
        if node is None:
            node = self.root
            return
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.val, end=' ')
    
    def in_order_traversal(self, node=None):
        if node is None:
            node = self.root
            return
        if node:
            self.in_order_traversal(node.left)
            print(node.val, end=' ')
            self.in_order_traversal(node.right)
    
# create a FullBinaryTree object
tree = FullBinaryTree()

# insert 10 random values between 1 and 100
for i in range(10):
    tree.insert(random.randint(1, 100))

# find min and max values
print("Min value:", tree.find_min())
print("Max value:", tree.find_max())

# calculate sum of all values
print("Sum of values:", tree.calculate_sum())

# perform pre-order traversal
print("Pre-order traversal:")
tree.pre_order_traversal(tree.root)


# perform post-order traversal
print("Post-order traversal:")
tree.post_order_traversal(tree.root)


# perform in-order traversal
print("In-order traversal:")
tree.in_order_traversal(tree.root)
# perform in-order traversal
print("In-order traversal:")
tree.in_order_traversal(tree.root)
