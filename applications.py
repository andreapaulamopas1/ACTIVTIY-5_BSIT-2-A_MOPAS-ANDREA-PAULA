from linked_stack import LinkedStack
from linked_queue import LinkedQueue


def check_balanced_parentheses(text):
    """Check (), [], and {} using a stack."""
    stack = LinkedStack()
    matching = {")": "(", "]": "[", "}": "{"}

    for character in text:
        if character in "([{":
            stack.push(character)
        elif character in ")]}":
            if stack.is_empty():
                return False
            if stack.pop() != matching[character]:
                return False

    return stack.is_empty()


def print_queue_simulation():
    """Add print jobs and process them in first-in, first-out order."""
    queue = LinkedQueue()
    print("\nPRINT QUEUE SIMULATION")
    print("Enter print jobs. Type 'done' as the job ID to stop adding jobs.")

    while True:
        job_id = input("Job ID: ").strip()
        if job_id.lower() == "done":
            break
        if not job_id:
            print("Job ID cannot be empty.")
            continue

        try:
            pages = int(input("Number of pages: "))
            if pages <= 0:
                print("Page count must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a whole number for the page count.")
            continue

        queue.enqueue({"id": job_id, "pages": pages})
        print("Job added.")

    if queue.is_empty():
        print("There are no print jobs.")
        return

    print("\nPrinting jobs in FIFO order:")
    wait_position = 1
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"Wait order {wait_position}: Job {job['id']} - {job['pages']} page(s)")
        wait_position += 1


def run_applications():
    while True:
        print("\nAPPLICATION EXERCISES")
        print("1. Check balanced parentheses")
        print("2. Simulate a print queue")
        print("3. Back to main menu")
        choice = input("Choose: ").strip()

        if choice == "1":
            expression = input("Enter text with brackets: ")
            if check_balanced_parentheses(expression):
                print("The brackets are balanced.")
            else:
                print("The brackets are NOT balanced.")
        elif choice == "2":
            print_queue_simulation()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
