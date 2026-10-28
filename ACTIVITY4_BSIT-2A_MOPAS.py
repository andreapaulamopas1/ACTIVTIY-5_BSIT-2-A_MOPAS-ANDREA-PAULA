
class Person:
    def __init__(self, firstname, lastname, age, program):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.program = program

    def __repr__(self):
        return f"{self.firstname} {self.lastname}, {self.age}, {self.program}"

def quickSortString01(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSortString01(left) + middle + quickSortString01(right)

def getPersonKey02(person, criteria):
    key = []

    for c in criteria:
        c = c.strip().lower()

        if c == "age":
            key.append(person.age)

        elif c in ["firstname", "first name"]:
            key.append(person.firstname.lower())

        elif c in ["last name", "lastname"]:
            key.append(person.lastname.lower())

        elif c == "program":
            key.append(person.program.lower())

    return tuple(key)

def quickSortPersons(arr, criteria):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    pivotKey = getPersonKey02(pivot, criteria)

    left = [
        x for x in arr
        if getPersonKey02(x, criteria) < pivotKey
    ]

    middle = [
        x for x in arr
        if getPersonKey02(x, criteria) == pivotKey
    ]

    right = [
        x for x in arr
        if getPersonKey02(x, criteria) > pivotKey
    ]

    return quickSortPersons(left, criteria) + middle + quickSortPersons(right, criteria)

if __name__ == "__main__":

    personArray = [
        Person("Paula", "Mopas", 21, "BSIT"),
        Person("Cherry", "Servo", 21, "BSN"),
        Person("Keana", "Aralar", 21, "BEED"),
        Person("Hannah", "Lim", 18, "BSN"),
        Person("Kim", "Uy", 19, "BSRT"),
        Person("Kelly", "Scott", 18, "BSN")
    ]

    print("Activity 4: Sorting (Quick Sort)\n")

    for person in personArray:
        print(person.firstname)

    print("\nAvailable criteria: Age, First Name, Last Name, Program")

    userInput = input("Enter how you want to arrange: ")

    criteria = [
        c.strip()
        for c in userInput.split(",")
        if c.strip() != ""
    ]

    if not criteria:
        print("No valid criteria entered.")
    else:
        sortedPersons = quickSortPersons(personArray, criteria)

        print("\nSorted Persons:")

        for person in sortedPersons:
            print(person)

