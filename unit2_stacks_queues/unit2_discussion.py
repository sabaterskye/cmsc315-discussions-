

"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)
        # The latest flight-plan change is placed on top and will be undone first.

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        # Peek lets a pilot or planner view the latest change without removing it.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)
        # Aircraft join the back of the queue, preserving their arrival order.

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")
        # Front shows which aircraft is next without removing it from the queue.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
    print("Exploring data structures through aviation scenarios.")

    # ===============================
    # STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: FLIGHT-PLAN EDITING ===")

    flight_plan = Stack()

    print("Recording changes made while preparing a flight plan...")
    changes = [
        "Entered departure airport: KSBY",
        "Added destination airport: KDOV",
        "Added planned cruising altitude: 6,000 feet",
        "Updated route to avoid restricted airspace"
    ]

    for change in changes:
        flight_plan.push(change)
        print(f"Saved change: {change}")

    print(f"\nMost recent change: {flight_plan.peek()}")
    print("\nUndoing flight-plan changes using LIFO:")
    print("The last change made will be undone first.")

    while not flight_plan.is_empty():
        print(f"Undoing: {flight_plan.pop()}")

    print(f"Are all changes removed? {flight_plan.is_empty()}")

    # Test popping from an empty stack.
    try:
        flight_plan.pop()
    except IndexError as error:
        print(f"Empty-stack pop test: {error}")

    # Test peeking at an empty stack.
    try:
        flight_plan.peek()
    except IndexError as error:
        print(f"Empty-stack peek test: {error}")

    # Test a stack containing only one item.
    single_stack = Stack()
    single_stack.push("Set departure airport to KSBY")
    print(f"\nSingle-item stack: {single_stack.peek()}")
    print(f"Removed change: {single_stack.pop()}")
    print(f"Is the single-item stack empty? {single_stack.is_empty()}")

    # Real-world scenario: Undoing changes to a flight plan.
    print("\nReal-world scenario: Flight-plan revision history")
    print("A flight planner makes several changes and needs to undo the latest one.")
    undo_history = Stack()
    undo_history.push("Original route entered")
    undo_history.push("Alternate airport added")
    undo_history.push("Cruising altitude updated")

    print(f"Latest revision to undo: {undo_history.pop()}")
    print(f"Previous revision to undo: {undo_history.pop()}")

    # ===============================
    # QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: AIRCRAFT MAINTENANCE ===")

    maintenance_queue = Queue()

    print("Aircraft are arriving for scheduled maintenance inspections...")
    aircraft = [
        "Aircraft N123AB",
        "Aircraft N456CD",
        "Aircraft N789EF",
        "Aircraft N321GH"
    ]

    for plane in aircraft:
        maintenance_queue.enqueue(plane)
        print(f"Added to maintenance queue: {plane}")

    print(f"\nNext aircraft for inspection: {maintenance_queue.front()}")
    print("\nProcessing aircraft using FIFO:")
    print("The first aircraft to arrive will be inspected first.")

    while not maintenance_queue.is_empty():
        print(f"Now inspecting: {maintenance_queue.dequeue()}")

    print(f"Is the maintenance queue empty? {maintenance_queue.is_empty()}")

    # Test dequeuing from an empty queue.
    try:
        maintenance_queue.dequeue()
    except IndexError as error:
        print(f"Empty-queue dequeue test: {error}")

    # Test viewing the front of an empty queue.
    try:
        maintenance_queue.front()
    except IndexError as error:
        print(f"Empty-queue front test: {error}")

    # Test a queue containing only one item.
    single_queue = Queue()
    single_queue.enqueue("Aircraft N555JK")
    print(f"\nSingle-aircraft queue front: {single_queue.front()}")
    print(f"Aircraft removed from queue: {single_queue.dequeue()}")
    print(f"Is the single-aircraft queue empty? {single_queue.is_empty()}")

    # Real-world scenario: Aircraft waiting for maintenance inspections.
    print("\nReal-world scenario: Maintenance inspection scheduling")
    request_queue = Queue()
    request_queue.enqueue("Aircraft N101AA: Routine inspection")
    request_queue.enqueue("Aircraft N202BB: Tire inspection")
    request_queue.enqueue("Aircraft N303CC: Engine inspection")

    print("Processing maintenance requests in arrival order:")
    while not request_queue.is_empty():
        print(f"Processing: {request_queue.dequeue()}")


if __name__ == "__main__":
    main()
