# Structures
class Node:
	
	# Create a Node with given value, and attach null nodes as child
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		if value is not None:
			self.left = Node(None)
			self.right = Node(None)
	
	# Check if current node is null node
	# If true, assign value and attach null nodes as children
	# If false, compare to current value and traverse to left/right child
	def insert(self,vIn):
		if self.value is None:
			self.value = vIn
			self.left = Node(None)
			self.right = Node(None)
		else:
			if vIn < self.value:
				self.left.insert(vIn)
			elif vIn > self.value:
				self.right.insert(vIn)
			else:
				print("Insertion Denied, Duplicate Entry: " + vIn)

    # Recursively compose an inorder string representation of the BST
	def getString(self):
		if self.value is None:
			return ""
		else:
			return "" + self.left.getString() + str(self.value) + self.right.getString()


	# Find and remove target node
	def remove(self, value):
		print("Removing " + str(value) + " at " + str(self.value))
		if self.value > value:
			if self.left.value is None:
				return self
			else:
				self.left = self.left.remove(value)
				return self
		elif self.value < value:
			if self.right.value is None:
				return self
			else:
				self.right = self.right.remove(value)
				return self
		# Target Node to remove has been found
		else:

			# If target has a right child
			# Find minimum under right child
			# Replace current value with right minimum value, than remove minimum from right child
			if self.right.value is not None:
				rightMin = self.right.findMin()
				self.value = rightMin.value
				self.right = self.right.remove(rightMin.value)
				return self

			# If target has no right child
			else:

				# If target has a left child
				# Replace with left child 
				if self.left.value is not None:
					return self.left

				# If target has no left child
				else:
					return Node(None)

	# Retreive and delete left-most node
	# Recursively trace to the left child
	# Return current node if left child is a Null Node 
	def findMin(self):
		if self.left.value is not None:
			return self.left.findMin()
		else:
			return self
			

			

			

# Scripting Zone
bst = Node(3)
print(bst.getString())
bst.insert(1)
print(bst.getString())
bst.insert(5)
print(bst.getString())
bst.insert(4)
print(bst.getString())
bst.insert(2)
print(bst.getString())
bst.insert(9)
print(bst.getString())
bst.insert(6)
print(bst.getString())
bst.insert(8)
print(bst.getString())
bst.insert(7)
print(bst.getString())

bst = bst.remove(3)
print(bst.getString())

bst = bst.remove(6)
print(bst.getString())

bst = bst.remove(5)
print(bst.getString())

bst = bst.remove(9)
print(bst.getString())

bst = bst.remove(2)
print(bst.getString())

bst.insert(5)
bst.insert(6)
bst.insert(3)
bst.insert(9)
bst.insert(2)
print(bst.getString())


		