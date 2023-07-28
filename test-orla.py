my_list = ["Orla", "Coffee", "Latte", "Americano"]
contents = [68, 5000, 4500, 5000]

price = []
for l, c in enumerate(my_list):
    x = c + str(contents[l])
    price.append(x)

print(price)

list_exes = ["CYMT", "MTRH", "MTH", "APSO"]
duration = [3, 6, 3, 6]

time = []
for e, u in enumerate(list_exes):
    y = u + " " + str(duration[e]) + "months"
    time.append(y)

print(time)
