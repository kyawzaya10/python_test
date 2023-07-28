my_list = [1, 2, "stop", 3, 4, "stop", 5, 6]

for x in my_list:
    if x == "stop":
        break
    print(x)

my_list = [1, 2, "cont", 3, 4, "cont", 5, 6]

for x in my_list:
    if x == "cont":
        continue
    print(x)

num = 0
while num < 5:
    num += 1  # num = num +1
    print("num is ", num)
