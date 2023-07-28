names_grades = {
    "Bill Gates": 65,
    "Steve Jobs": 85,
    "James Bond": 45,
    "John Smith": 55,
    "Eward Coke": 35
}

names = [x.split()[0] for x, y in names_grades.items() if y > 50]
print(names)

name_gradez = {
    "John Wick": 75,
    "Barry Allen": 75,
    "Erling Haaland": 90,
    "Kevin DeBruyne": 90
}

namez = [f.split()[0] for f, l in name_gradez.items() if l > 50]
print(namez)
