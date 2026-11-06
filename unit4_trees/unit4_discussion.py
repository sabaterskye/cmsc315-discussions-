
"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================
This program uses an aviation flight plan to demonstrate
how a Binary Search Tree organizes and searches call signs.
"""


class Node:
    def __init__(self, value):
        # Store the call sign and child references.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Start with an empty flight plan.
        self.root = None

    def insert(self, value):
        # Start insertion at the root of the tree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Create a new node when an empty position is found.
        if node is None:
            return Node(value)

        # Smaller call signs go left; larger ones go right.
        # This keeps the tree organized for faster searching.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate call signs are ignored.
        return node

    def search(self, value):
        # Begin searching from the root.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        # An empty position means the call sign was not found.
        if node is None:
            return False

        if value == node.value:
            return True

        # Only search the side where the value could be.
        # This avoids checking every node like linear search.
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        # Collect call signs in sorted order.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        if node is not None:
            # Visit left, current node, then right.
            # Since smaller values are on the left and larger
            # values are on the right, the result is sorted.
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: AVIATION BINARY SEARCH TREE ===")

    # ===============================
    # BUILD THE FLIGHT PLAN
    # ===============================

    flight_plan = BST()

    # Original aircraft call signs for this example.
    call_signs = [
        "EAGLE",
        "FALCON",
        "HAWK",
        "JET",
        "RAVEN",
        "SKY",
        "VIPER"
    ]

    print("\n=== FLIGHT PLAN CONSTRUCTION ===")

    for call_sign in call_signs:
        flight_plan.insert(call_sign)
        print("Added aircraft:", call_sign)

    # Each call sign is placed left or right based on
    # alphabetical order, reducing the search area.

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================

    print("\n=== IN-ORDER TRAVERSAL ===")

    sorted_flight_plan = flight_plan.inorder()

    print("Organized call signs:", sorted_flight_plan)

    # In-order traversal visits left, root, and right.
    # This produces alphabetical order in our BST.

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== FLIGHT PLAN SEARCH TESTS ===")

    # These call signs are already in the flight plan.
    print("EAGLE found:", flight_plan.search("EAGLE"))
    print("RAVEN found:", flight_plan.search("RAVEN"))

    # These call signs were never added.
    print("COBRA found:", flight_plan.search("COBRA"))
    print("TIGER found:", flight_plan.search("TIGER"))

    # The BST compares each value and only follows
    # the left or right branch needed to find it.

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Test searching and traversing an empty flight plan.
    empty_plan = BST()

    print("Empty plan search:", empty_plan.search("EAGLE"))
    print("Empty plan traversal:", empty_plan.inorder())

    # Test inserting a duplicate call sign.
    flight_plan.insert("EAGLE")
    print("After duplicate insertion:", flight_plan.inorder())

    # Duplicate values are ignored, so the flight plan
    # does not contain the same call sign twice.

    # Test a tree containing only one aircraft.
    single_flight = BST()
    single_flight.insert("SOLO")

    print("Single aircraft plan:", single_flight.inorder())
    print("SOLO found:", single_flight.search("SOLO"))


if __name__ == "__main__":
    main()
