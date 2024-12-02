from typing import Optional

class Node():
    def __init__(self, start: int, end: int):
        """
        Initializes a Node object representing an event in the calendar.

        Args:
        - start (int): Start time of the event.
        - end (int): End time of the event.
        """
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None  # Left child for earlier events
        self.right_child: Optional[Node] = None  # Right child for later events

    def insert(self, node: 'Node') -> bool:
        """
        Attempts to insert a new event into the binary tree.

        Args:
        - node (Node): The new event to be inserted.

        Returns:
        - bool: True if the event is successfully added; False if it overlaps with an existing event.
        """
        # Check if the new event overlaps with the current event
        if node.start < self.end and node.end > self.start:
            return False

            # Insert into the left subtree if the new event ends before the current event starts
        if node.end <= self.start:
            if not self.left_child:
                self.left_child = node  # Insert as the left child if the slot is empty
                return True
            return self.left_child.insert(node)  # Recursively attempt insertion in the left subtree

        # Insert into the right subtree if the new event starts after the current event ends
        if node.start >= self.end:
            if not self.right_child:
                self.right_child = node  # Insert as the right child if the slot is empty
                return True
            return self.right_child.insert(node)  # Recursively attempt insertion in the right subtree




class Calendar():
    def __init__(self):
        """
        Initializes an empty Calendar object.
        """
        self.root: Node = None  # Root node of the binary tree storing events

    def book(self, start: int, end: int) -> bool:
        """
        Schedules a new event if it does not cause a double booking.

        Args:
        - start (int): Start time of the event.
        - end (int): End time of the event.

        Returns:
        - bool: True if the event is successfully added; False otherwise.
        """
        # If the tree is empty, insert the first event as the root
        if self.root is None:
            self.root = Node(start=start, end=end)
            return True
        # Attempt to insert the new event into the binary tree
        return self.root.insert(Node(start, end))


# Example Usage
calendar = Calendar()

# Test cases
print(calendar.book(5, 10))  # True: Successfully added as the first event
print(calendar.book(8, 13))  # False: Overlaps with the event [5, 10)
print(calendar.book(10, 15))  # True: Successfully added after [5, 10)
