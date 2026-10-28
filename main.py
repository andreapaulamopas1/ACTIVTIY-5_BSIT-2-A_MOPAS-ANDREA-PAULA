from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import run_applications


def read_capacity():
    while True:
        try:
            capacity = int(input("Enter capacity (positive whole number): "))
            if capacity > 0:
                return capacity
            print("Capacity must be greater than 0.")
        except ValueError:
            print("Please enter a whole number.")


def use_structure(structure, structure_type):
    while True:
        print("\nOperations:")
        if "Stack" in structure_type:
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
        else:
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek front")
        print("4. Check if empty")
        print("5. Check if full")
        print("6. Return to main menu")

        choice = input("Choose an operation: ").strip()

        try:
            if choice == "1":
                value = input("Enter a value: ")
                if "Stack" in structure_type:
                    structure.push(value)
                else:
                    structure.enqueue(value)
                print("Value added.")
            elif choice == "2":
                if "Stack" in structure_type:
                    print("Removed:", structure.pop())
                else:
                    print("Removed:", structure.dequeue())
            elif choice == "3":
                if "Stack" in structure_type:
                    print("Top value:", structure.peek())
                else:
                    print("Front value:", structure.peek_front())
            elif choice == "4":
                print("Empty:", structure.is_empty())
            elif choice == "5":
                print("Full:", structure.is_full())
            elif choice == "6":
                break
            else:
                print("Invalid choice.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)

        print("Current state:", structure)


def main():
    while True:
        print("\nSTACKS AND QUEUES LAB")
        print("1. Array Stack")
        print("2. Linked List Stack")
        print("3. Circular Array Queue")
        print("4. Linked List Queue")
        print("5. Application Exercises")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            capacity = read_capacity()
            use_structure(ArrayStack(capacity), "ArrayStack")
        elif choice == "2":
            use_structure(LinkedStack(), "LinkedStack")
        elif choice == "3":
            capacity = read_capacity()
            use_structure(ArrayQueue(capacity), "ArrayQueue")
        elif choice == "4":
            use_structure(LinkedQueue(), "LinkedQueue")
        elif choice == "5":
            run_applications()
        elif choice == "6":
            print("Program ended. Thank you!")
            break
        else:
            print("Invalid choice. Please choose from 1 to 6.")


if __name__ == "__main__":
    main()
