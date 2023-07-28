names = ["Mg Mg", "Aung Aung", "Hla Hla"]
salaries = [2000, 3000, 4000]

names_salaries = []
for i, v in enumerate(names):
    x = v + " $" + str(salaries[i])
    names_salaries.append(x)

print(names_salaries)
