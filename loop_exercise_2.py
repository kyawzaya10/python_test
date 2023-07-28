"""
names_grades = {
    "Bill Gates":65,
    "Steve Jobs":85,
    "James Bond":45,
    "John Smith":55,
    "Eward Coke":35
}
items(), if grade > 50, split()[0]
names = ["Bill", "Steve", "John"]
"""

names_grades = {
    "Bill Gates":65,
    "Steve Jobs":85,
    "James Bond":45,
    "John Smith":55,
    "Eward Coke":35
}
names = [name.split()[0] for name, grade in names_grades.items() if grade > 50]
print(names)