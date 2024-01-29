# The class Node and class Link_list creates a singly linked list

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class Linked_list:
    def __init__(self):
        self.head_value = None

    def print_linked_list(self):  # This prints out the entire list
        print_value = self.head_value
        while print_value is not None:
            print(print_value.value)
            print_value = print_value.next_node

    def Insert_Beginning(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next value to existing node
        NewNode.next_node = self.head_value
        self.head_value = NewNode

    # Function call to insert a new node at the end of the link list
    def Insert_End(self, newdata):
        NewNode = Node(newdata)
        if self.head_value is None:
            self.head_value = NewNode
            return
        laste = self.head_value
        while (laste.next_node):
            laste = laste.next_node
        laste.next_node = NewNode

        # Function to add node between two nodes

    def Insert_Between(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.next_node = middle_node.next_node
        middle_node.next_node = NewNode

        # Function to remove node

    def Remove_Node(self, Removekey):
        HeadVal = self.head_value

        if HeadVal is not None:
            if HeadVal.value == Removekey:
                self.head_value = HeadVal.next_node
                HeadVal = None
                return
            while HeadVal is not None:
                if HeadVal.value == Removekey:
                    break
                prev = HeadVal
                HeadVal = HeadVal.next_node
            if HeadVal == None:
                return
            prev.next_node = HeadVal.next_node
            HeadVal = None


# Creating the values of the linked list
list_name = Linked_list()
# Creating the first ("head") value of the list
list_name.head_value = Node('Mon')
# Creating the other nodes
e2 = Node('Tue')
e3 = Node('Wed')
e4 = Node('Thu')

# Creating the pointers from one node to the next node
list_name.head_value.next_node = e3
e3.next_node = e4
e4.next_node = e2

# Function call to print out the entire list
# list_name.print_linked_list()

# Function call to insert  new node at the begining of the link list
# list_name.Insert_Beginning()

# Function call to insert new node at the end of the link list
# list_name.Insert_End("Fri")
# list_name.print_linked_list()

# Function call to insert new node in the link list
list_name.Insert_Between(list_name.head_value, "Test")  # Inserted in the next node after the head node
list_name.Insert_Between(e3, "Test2")  # Inserted in the next node after node e3
list_name.print_linked_list()

# Function call to remove a node in the link list
list_name.Remove_Node("Test")
list_name.print_linked_list()

# print(e2.value)
