class Node:

    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    
    if node == None: return []
    
    values = [node.value]
    nodes = [node]
    elements_sortedbylevels(nodes, values)
    return values
    
def elements_sortedbylevels(nodes, values):

    list_nodes = []
    
    for node in nodes:
        if node.left != None:
            values.append(node.left.value)
            list_nodes.append(node.left)
        if node.right != None:
            values.append(node.right.value)
            list_nodes.append(node.right)
    
    if len(list_nodes) > 0: elements_sortedbylevels(list_nodes, values)


print(tree_by_levels(Node(Node(None, Node(None, None, 9), 7), Node(Node(None, None, 5), Node(None, None, 2), 33), 13)))









