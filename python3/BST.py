# Structures
class Node:
	"""docstring for Node"""
	def __init__(self, value):
		self.value = value
		if value is not None:
			self.left = Node(None)
			self.right = Node(None)
		
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

	def getString(self):
		if self.value is None:
			return ""
		else:
			return "" + self.left.getString() + str(self.value) + self.right.getString()

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


		