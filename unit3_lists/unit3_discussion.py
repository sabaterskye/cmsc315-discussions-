"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""



def insert_at(lst, index, value):
    # Insert the value at the selected position.
    # Existing elements shift to the right to make room.
    # Inserting at the beginning takes longer because more elements shift.
    # Inserting at the end is generally faster.
    lst.insert(index, value)


def delete_at(lst, index):
    # Check that the index is valid before deleting anything.
    # This prevents errors when trying to remove an item that doesn't exist.
    if index < 0 or index >= len(lst):
        return None

    # Remove and return the selected value.
    # Remaining elements shift left to fill the empty space.
    return lst.pop(index)


def search_value(lst, value):
    # This is a linear search because it checks each item one at a time.
    # It scans from beginning to end until it finds a match.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 if the value isn't in the list.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================

    print("\n=== INSERTION TESTS ===")

    # These represent flight details in a pilot's flight plan.
    flight_plan = ["Preflight", "Taxi", "Takeoff", "Cruise"]

    print("Original flight plan:", flight_plan)

    # Insert at the beginning.
    insert_at(flight_plan, 0, "Weather Check")
    print("After beginning insertion:", flight_plan)

    # Insert in the middle.
    insert_at(flight_plan, 3, "Climb")
    print("After middle insertion:", flight_plan)

    # Insert at the end.
    insert_at(flight_plan, len(flight_plan), "Landing")
    print("After end insertion:", flight_plan)

    # ===============================
    # DELETION TESTS
    # ===============================

    print("\n=== DELETION TESTS ===")

    # Remove the first item.
    removed = delete_at(flight_plan, 0)
    print("Removed from beginning:", removed)
    print("Updated flight plan:", flight_plan)

    # Remove an item from the middle.
    removed = delete_at(flight_plan, 2)
    print("Removed from middle:", removed)
    print("Updated flight plan:", flight_plan)

    # Remove the last item.
    removed = delete_at(flight_plan, len(flight_plan) - 1)
    print("Removed from end:", removed)
    print("Updated flight plan:", flight_plan)

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    # Search for an item that exists.
    result = search_value(flight_plan, "Takeoff")
    print("Takeoff found at index:", result)

    # Search for an item that doesn't exist.
    result = search_value(flight_plan, "Parking")
    print("Parking search result:", result)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Try deleting with an invalid index.
    result = delete_at(flight_plan, 20)
    print("Invalid deletion result:", result)

    # Try deleting from an empty list.
    empty_list = []
    result = delete_at(empty_list, 0)
    print("Deleting from empty list:", result)

    # Insert into an empty list.
    insert_at(empty_list, 0, "Preflight")
    print("After inserting into empty list:", empty_list)


if __name__ == "__main__":
    main()
