"""Implementing of binary search tree"""

__author__ = "Stanislav Hrytsyshyn"


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    @staticmethod
    def create_node(node, value):
        node.left = Node()
        node.right = Node()
        node.value = value

    @staticmethod
    def insert_value(node, value):
        if not Node.is_node_exist(node):
            Node.create_node(node, value)
        elif value < node.value:
            Node.insert_value(node.left, value)
        elif value >= node.value:
            Node.insert_value(node.right, value)

    @staticmethod
    def search_value(node, value):
        if not Node.is_node_exist(node):
            result = None
        elif node.value == value:
            result = node
        elif value < node.value:
            result = Node.search_value(node.left, value)
        elif value > node.value:
            result = Node.search_value(node.right, value)
        
        return result
    
    @staticmethod
    def get_min_node(node):
        if not Node.is_node_exist(node):
            result = None
        elif not Node.is_node_exist(node.left):
            result = node
        else:
            result = Node.get_min_node(node.left)
        
        return result

    @staticmethod
    def get_max_node(node):
        if not Node.is_node_exist(node):
            result = None
        elif not Node.is_node_exist(node.right):
            result = node
        else:
            result = Node.get_max_node(node.right)
        
        return result
    
    @staticmethod
    def get_node_child_count(node):
        children_count = 0

        children_count = children_count + 1 if Node.is_node_exist(node.left) else children_count
        children_count = children_count + 1 if Node.is_node_exist(node.right) else children_count

        return children_count
    
    @staticmethod
    def get_child_or_none(node):
        return node.left if Node.is_node_exist(node.left) else node.right

    @staticmethod
    def transplant_node(to_node, from_node):
        to_node.value = from_node.value
        to_node.left = from_node.left
        to_node.right = from_node.right

    @staticmethod
    def delete_node_with_one_or_zero_childs(node):
        child_or_none = Node.get_child_or_none(node)
        Node.transplant_node(node, child_or_none)
    
    @staticmethod
    def delete_full_node(root, value):
        searched_node = Node.search_value(root, value)
        if not Node.is_node_exist(searched_node):
            print('No such value')
            return False
        
        node_child_count = Node.get_node_child_count(searched_node)

        if node_child_count <= 1:
            Node.delete_node_with_one_or_zero_childs(searched_node)
        else:
            min_right_node = Node.get_min_node(searched_node.right)
            searched_node.value = min_right_node
            Node.delete_node_with_one_or_zero_childs(min_right_node)

        return True

    @staticmethod
    def symetric_node_traversal(node):
        result = []
        if not Node.is_node_exist(node):
            return result
        result.extend(Node.symetric_node_traversal(node.left))
        result.append(node.value)
        result.extend(Node.symetric_node_traversal(node.right))

        return result

    @staticmethod
    def post_order_node_traversal(node):
        result = []
        if not Node.is_node_exist(node):
            return result
        result.extend(Node.symetric_node_traversal(node.left))
        result.extend(Node.symetric_node_traversal(node.right))
        result.append(node.value)

        return result

    @staticmethod
    def pre_order_node_traversal(node):
        result = []
        if not Node.is_node_exist(node):
            return result
        result.append(node.value)
        result.extend(Node.symetric_node_traversal(node.left))
        result.extend(Node.symetric_node_traversal(node.right))

        return result

    @staticmethod
    def is_node_exist(node):
        return node and node.value 


if __name__ == "__main__":
    node = Node()

    for value in [9, 4, 5, 7, 8, 12, 14]:
        Node.insert_value(node, value)

    print(Node.symetric_node_traversal(node))
    print(Node.pre_order_node_traversal(node))
    print(Node.post_order_node_traversal(node))

    Node.delete_full_node(node, 7)
    print(Node.symetric_node_traversal(node))
