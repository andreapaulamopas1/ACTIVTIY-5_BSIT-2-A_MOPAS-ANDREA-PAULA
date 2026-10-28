# Stacks and Queues: Array vs. Linked List

## About the Program
This beginner-friendly Python program demonstrates four data structures:

1. `ArrayStack` - a stack stored in a fixed-size list.
2. `LinkedStack` - a stack made from linked nodes.
3. `ArrayQueue` - a queue stored in a circular array.
4. `LinkedQueue` - a queue made from linked nodes.

It also includes two application exercises:
- Checking whether `()`, `[]`, and `{}` are balanced.
- Simulating a print queue in FIFO order.

## Files
- `array_stack.py` - ArrayStack class.
- `linked_stack.py` - LinkedStack class.
- `array_queue.py` - ArrayQueue class.
- `linked_queue.py` - LinkedQueue class.
- `applications.py` - The two application exercises.
- `main.py` - The menu and test driver.
- `analysis.md` - Answer to the analysis question.

## Requirements
Python 3. No extra libraries are needed.

## How to Run
1. Download all the Python files into the same folder.
2. Open a terminal or command prompt in that folder.
3. Run:

   `python main.py`

   If your computer uses the `python3` command, run `python3 main.py` instead.

4. Choose an option from the menu.
5. Follow the prompts to perform operations.

## Example: Array Stack
- Choose `1` for Array Stack.
- Enter a capacity such as `3`.
- Choose `1` to push a value.
- Choose `3` to peek at the top value.
- Choose `2` to pop the top value.
- Try popping from an empty stack to see the underflow message.
- Try pushing more values than the capacity to see the overflow message.

## Notes
- A stack follows **LIFO**: Last In, First Out.
- A queue follows **FIFO**: First In, First Out.
- Array implementations have a fixed capacity.
- Linked-list implementations do not have a fixed capacity set by this program.
- `is_full()` always returns `False` for linked implementations because they do not use a fixed capacity.
